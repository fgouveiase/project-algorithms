from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(message="string", key="string")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(message=False, key=1)

    assert encrypt_message(message="felipe", key=9) == "epilef"
    assert encrypt_message(message="felipe", key=3) == "lef_epi"
    assert encrypt_message(message="felipe", key=4) == "ep_ilef"
