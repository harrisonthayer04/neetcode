from typing import Iterable, Tuple, List, Dict
import math


def _to_decimal_rate(r: float) -> float:
    """
    Normalize APR to a decimal. Accepts either percent (r > 1) or decimal (r <= 1).
    """
    return r / 100.0 if r > 1 else r


def monthly_payment(p0: float, r: float, n: int) -> float:
    """
    Compute level monthly payment for a fully amortizing loan.

    Parameters
    ----------
    p0 : float
        Principal (loan amount).
    r : float
        Annual Percentage Rate (APR). Can be decimal (0.079) or percent (7.9).
    n : int
        Number of months.

    Returns
    -------
    float
        Monthly payment.
    """
    if n <= 0:
        raise ValueError("Number of months n must be positive.")
    r = _to_decimal_rate(r)
    I = r / 12.0  # monthly rate

    if abs(I) < 1e-15:  # zero-interest case
        return p0 / n

    return (p0 * I) / (1.0 - (1.0 + I) ** (-n))


def current_balance(p_i: float, r: float, n_i: int, N_i: int) -> float:
    """
    Present value of the remaining N_i payments for an existing loan.

    Uses the stable PV-of-remaining-payments formula:
        Balance = M_i * (1 - (1 + I)^(-N_i)) / I
    where M_i is the original monthly payment and I = r/12.

    Parameters
    ----------
    p_i : float
        Original principal of the old loan.
    r : float
        APR of the old loan (decimal or percent).
    n_i : int
        Original term in months.
    N_i : int
        Remaining months (from today).

    Returns
    -------
    float
        Current balance (amount needed to pay off the loan today).
    """
    if N_i < 0 or n_i <= 0 or N_i > n_i:
        raise ValueError("Require 0 <= N_i <= n_i and n_i > 0.")
    r = _to_decimal_rate(r)
    I = r / 12.0
    M_i = monthly_payment(p_i, r, n_i)

    if abs(I) < 1e-15:
        return M_i * N_i

    return M_i * (1.0 - (1.0 + I) ** (-N_i)) / I


def consolidate_loans(
    old_loans: Iterable[Tuple[float, float, int, int]],
    r_new: float,
    n_new: int,
) -> Tuple[float, float, float, Dict[str, List[float]]]:
    """
    Sum current balances of old loans -> new principal P_o, compute new payment M_o,
    and total dollars saved vs. keeping the old loans.

    Parameters
    ----------
    old_loans : iterable of (P_i, r_i, n_i, N_i)
        Each tuple/list: original principal, APR, original months, remaining months.
    r_new : float
        New APR (decimal or percent).
    n_new : int
        New term in months.

    Returns
    -------
    (P_o, M_o, saved, details) : tuple
        P_o : float
            Sum of current balances (new principal).
        M_o : float
            New monthly payment.
        saved : float
            (Sum of remaining old payments) - (total new payments).
        details : dict
            Per-loan 'M_old' and 'BalancesNow' lists for inspection.
    """
    balances: List[float] = []
    M_old: List[float] = []
    total_old_remaining = 0.0

    for P_i, r_i, n_i, N_i in old_loans:
        bal = current_balance(P_i, r_i, n_i, N_i)
        M_i = monthly_payment(P_i, r_i, n_i)
        balances.append(bal)
        M_old.append(M_i)
        total_old_remaining += M_i * N_i

    P_o = sum(balances)
    M_o = monthly_payment(P_o, r_new, n_new)
    total_new = M_o * n_new
    saved = total_old_remaining - total_new

    details = {
        "M_old": M_old,
        "BalancesNow": balances,
        "total_old_remaining": [total_old_remaining],
        "total_new": [total_new],
    }
    return P_o, M_o, saved, details


if __name__ == "__main__":
    # ----- Example (matches your MATLAB test) -----
    # Old loans: [25,000, 7.9%, 60, 37; 15,000, 12.9%, 48, 30]
    old_loans = [
        (25000.0, 7.9, 60, 37),
        (15000.0, 12.9, 48, 30),
    ]
    # New loan: [3.9%, 60]
    r_new = 3.9
    n_new = 60

    P_o, M_o, saved, S = consolidate_loans(old_loans, r_new, n_new)

    print(f"New loan amount (P_o): ${P_o:,.2f}")
    print(f"New monthly payment (M_o): ${M_o:,.2f}")
    print(f"Total amount saved: ${saved:,.2f}\n")

    # Optional detail printouts
    print("Per-loan monthly payments (old):", [round(x, 4) for x in S["M_old"]])
    print("Per-loan current balances:      ", [round(x, 2) for x in S["BalancesNow"]])

    # Simple sanity checks against earlier MATLAB outputs:
    # P_o ≈ 26812.17, M_o ≈ 492.58, saved ≈ 1206.81
    assert math.isclose(P_o, 26812.17, rel_tol=0, abs_tol=0.5)
    assert math.isclose(M_o, 492.58,   rel_tol=0, abs_tol=0.5)
    assert math.isclose(saved, 1206.81, rel_tol=0, abs_tol=2.0)
