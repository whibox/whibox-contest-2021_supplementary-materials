from nist_p256 import NIST_P256
from commands import ecdsa_verify


# key pairs
d = 0x9C29EDDAEF2C2B4452052B668B83BE6365004278068884FA1AC3F6D0622875C3
Q_x = 0x78E0E9DACCC47DE94D674DF3B35624A2F08E600B26B3444077022AD575AF4DB7
Q_y = 0x3084B4B8657EEA12396FDE260432BA7BDB3E092D61A42F830150D6CC8D798F9F

# message and random key
# echo -n CHES2021 | sha256sum
hash_ = 0xf7fd41e28dfcca32c1ceef637c202ca6e99e57f18afef957df0866b4cdd60f5c

# cat test_hash | ./dECDSA
r = 0x8007abc1cd96650531bd8039893e8cf549a52d26e2a8a0e4700087523a7156a4
s = 0x2794de699028d0768259367ad4676bfe2dacca139263a684d0a7434ea3842bc4


def test_test_vectors():
    Q = NIST_P256.Point(
        NIST_P256.Modular(Q_x),
        NIST_P256.Modular(Q_y),
    )
    assert ecdsa_verify(Q, hash_, (r, s))
