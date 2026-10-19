
def test_Login(AOS_Driver):
    AOS_Driver.Login_Error()

def test_Login_out(AOS_Driver):
    AOS_Driver.Login()
    AOS_Driver.Logout()

def test_Join(AOS_Driver):
    AOS_Driver.Login()
    AOS_Driver.join_membership()