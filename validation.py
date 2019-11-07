from constants import KWErrorCode

if __name__ == "__main__":
    # constants 검사
    for error in KWErrorCode:
        print(error)

    assert (KWErrorCode.OP_ERR_NONE == KWErrorCode.OP_ERR_NONE)
    assert (KWErrorCode.OP_ERR_NONE != KWErrorCode.OP_ERR_ORD_OVERFLOW0)
    