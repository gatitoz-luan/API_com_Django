# credits: https://support.microsoft.com/en-us/office/pmt-function-0214da64-9a63-4996-bc20-214433fa6441

def payment(rate, nper, pv, fv=0, type=0):
    rate = rate / 12
    # rate  - interest rate per month
    # nper  - number of periods (months)
    # pv    - present value
    # fv    - future value
    # type  - when the payments are due:
    #        0: end of the period, e.g. end of month (default)
    #        1: beginning of period
    if rate == 0:
        return -((pv + fv) / nper)

    pvif = pow(1.0 + rate, nper)

    pmt = rate / (pvif - 1.0) * -(pv * pvif + fv)

    if type == 1:
        pmt /= (1.0 + rate)

    return pmt