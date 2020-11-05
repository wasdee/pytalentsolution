from pytalentsolution import Tenant


def test_main():
    t = Tenant(external_id="123")
    
    t.create()
    assert t.name

    t.delete()
    assert t.name is None