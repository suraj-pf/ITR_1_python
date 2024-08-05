from fastapi import FastAPI
from pydantic import BaseModel

# Create an instance of FastAPI
app = FastAPI()


# Define Pydantic models for request validation
class Amount(BaseModel):
    amount: float


class Donation(BaseModel):
    amount: float
    choice: str
    ans: str


# Define endpoints for each deduction function
@app.post("/eighty_c/")
def eighty_c(amount: Amount):
    """
    Endpoint for Section 80C deductions.
    """
    return {"amount": amount.amount}


@app.post("/eighty_ccd1b/")
def eighty_ccd1b(amount: Amount):
    """
    Endpoint for Section 80CCD(1B) deductions.
    """
    return {"amount": amount.amount}


@app.post("/eighty_ccd2/")
def eighty_ccd2(amount: Amount):
    """
    Endpoint for Section 80CCD(2) deductions.
    """
    return {"amount": amount.amount}


@app.post("/eighty_d/")
def eighty_d(amount: Amount):
    """
    Endpoint for Section 80D deductions.
    """
    return {"amount": amount.amount}


@app.post("/eighty_dd/")
def eighty_dd(amount: Amount):
    """
    Endpoint for Section 80DD deductions.
    """
    return {"amount": amount.amount}


@app.post("/eighty_ddb/")
def eighty_ddb(amount: Amount):
    """
    Endpoint for Section 80DDB deductions.
    """
    return {"amount": amount.amount}


@app.post("/eighty_e/")
def eighty_e(amount: Amount):
    """
    Endpoint for Section 80E deductions.
    """
    return {"amount": amount.amount}


@app.post("/eighty_ee/")
def eighty_ee(amount: Amount):
    """
    Endpoint for Section 80EE deductions.
    """
    return {"amount": amount.amount}


@app.post("/eighty_eea/")
def eighty_eea(amount: Amount):
    """
    Endpoint for Section 80EEA deductions.
    """
    return {"amount": amount.amount}


@app.post("/eighty_eeb/")
def eighty_eeb(amount: Amount):
    """
    Endpoint for Section 80EEB deductions.
    """
    return {"amount": amount.amount}


@app.post("/eighty_g/")
def eighty_g(donation: Donation):
    """
    Endpoint for Section 80G deductions.
    Handles different categories of donations.
    """
    if donation.choice == "y":
        if donation.ans == "y":
            deduction = donation.amount
        else:
            deduction = donation.amount * 0.5
    else:
        if donation.ans == "y":
            deduction = donation.amount
        else:
            deduction = donation.amount * 0.5
    return {"deduction": deduction}


@app.post("/eighty_u/")
def eighty_u(amount: Amount):
    """
    Endpoint for Section 80U deductions.
    """
    return {"amount": amount.amount}


@app.post("/eighty_tta/")
def eighty_tta(amount: Amount):
    """
    Endpoint for Section 80TTA deductions.
    """
    return {"amount": amount.amount}


@app.post("/eighty_ttb/")
def eighty_ttb(amount: Amount):
    """
    Endpoint for Section 80TTB deductions.
    """
    return {"amount": amount.amount}


@app.post("/eighty_gga/")
def eighty_gga(amount: Amount):
    """
    Endpoint for Section 80GGA deductions.
    """
    return {"amount": amount.amount}


@app.post("/eighty_ggc/")
def eighty_ggc(amount: Amount):
    """
    Endpoint for Section 80GGC deductions.
    """
    return {"amount": amount.amount}


@app.post("/interest_housingloan/")
def interest_housingloan(amount: Amount):
    """
    Endpoint for deductions on interest paid on housing loans.
    """
    return {"amount": amount.amount}


@app.post("/otherdeductions/")
def otherdeductions(amount: Amount):
    """
    Endpoint for other miscellaneous deductions.
    """
    return {"amount": amount.amount}


class Deductions(BaseModel):
    de: float


@app.post("/deductions_for_old/")
def deductions_for_old(deductions: Deductions):
    """
    Endpoint for calculating total deductions under the old tax regime.
    """
    total_deductions_for_old = (
        eighty_c(Amount(amount=deductions.de)).get("amount")
        + eighty_ccd1b(Amount(amount=deductions.de)).get("amount")
        + eighty_ccd2(Amount(amount=deductions.de)).get("amount")
        + eighty_d(Amount(amount=deductions.de)).get("amount")
        + eighty_dd(Amount(amount=deductions.de)).get("amount")
        + eighty_ddb(Amount(amount=deductions.de)).get("amount")
        + eighty_e(Amount(amount=deductions.de)).get("amount")
        + eighty_ee(Amount(amount=deductions.de)).get("amount")
        + eighty_eea(Amount(amount=deductions.de)).get("amount")
        + eighty_eeb(Amount(amount=deductions.de)).get("amount")
        + eighty_g(Donation(amount=deductions.de, choice="y", ans="y")).get("deduction")
        + eighty_u(Amount(amount=deductions.de)).get("amount")
        + eighty_tta(Amount(amount=deductions.de)).get("amount")
        + eighty_ttb(Amount(amount=deductions.de)).get("amount")
        + eighty_gga(Amount(amount=deductions.de)).get("amount")
        + eighty_ggc(Amount(amount=deductions.de)).get("amount")
        + interest_housingloan(Amount(amount=deductions.de)).get("amount")
        + otherdeductions(Amount(amount=deductions.de)).get("amount")
    )
    return {"total_deductions_for_old": total_deductions_for_old}


@app.post("/deductions_for_new/")
def deductions_for_new(deductions: Deductions):
    """
    Endpoint for calculating total deductions under the new tax regime.
    """
    total_deductions_for_new = (
        eighty_ccd1b(Amount(amount=deductions.de)).get("amount")
        + eighty_ccd2(Amount(amount=deductions.de)).get("amount")
        + eighty_ee(Amount(amount=deductions.de)).get("amount")
        + eighty_eea(Amount(amount=deductions.de)).get("amount")
        + otherdeductions(Amount(amount=deductions.de)).get("amount")
    )
    return {"total_deductions_for_new": total_deductions_for_new}


# Additional endpoints for other functions if necessary

# Run the application
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
