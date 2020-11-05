from uuid import uuid4

from pytalentsolution import Tenant


def test_main():
    t = Tenant(external_id=uuid4().hex)

    t.create()
    assert t.name

    t2 = Tenant.get(t.name)
    assert t.name == t2.name

    tenants = Tenant.list()
    assert any((t.external_id == t2.external_id for t in tenants))

    # test update
    new = uuid4().hex
    t.external_id = new
    t.update()
    t3 = Tenant.get(t.name)
    assert t3.external_id == new

    t.delete()
    assert t.name is None
