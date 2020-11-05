from uuid import uuid4

import pytest

from pytalentsolution import Company, CompanySize


def test_main(tenant):
    c = Company(
            display_name=uuid4().hex,
            external_id=uuid4().hex
    )

    c.create(tenant)

    # test update
    new = uuid4().hex
    c.display_name = new
    c.size = CompanySize.BIG
    c.update()
    c2 = Company.get(c.name)
    assert c2.display_name == new
    assert c2.size == CompanySize.BIG

    companies = Company.list(tenant)
    assert any((c.external_id == c2.external_id for c in companies))

    c.delete()




