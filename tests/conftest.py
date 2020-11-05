from uuid import uuid4

import pytest

from pytalentsolution import Company, Tenant


@pytest.fixture
def tenant():
    t = Tenant(external_id=uuid4().hex)
    t.create()
    yield t
    t.delete()


@pytest.fixture
def company(tenant):
    c = Company(
            display_name="github",
            external_id=uuid4().hex
    )
    c.create(tenant)
    yield c
    c.delete()
