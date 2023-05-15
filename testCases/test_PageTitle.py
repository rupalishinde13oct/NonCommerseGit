


class TestPageTitle:

    def test_PageTirle_001(self , setup):

        self.d = setup

        if self.d.title == "Your store. Login":
            assert True
        else:
            assert False