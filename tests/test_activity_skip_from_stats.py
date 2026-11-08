# MyTraL: my trailing log
#
# Copyright (C) 2015-2026 Martin Dvorak <martin.dvorak@mindforger.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
import pytest

from mytral import commons
from mytral.backends import entities


@pytest.mark.mytral
@pytest.mark.parametrize(
    "name, tags, expected",
    [
        ("morning run", [], False),
        ("morning run", ["race"], False),
        (f"{commons.SKIP_FROM_STATS_NAME_MARKER} running", [], True),
        ("running", [commons.SKIP_FROM_STATS_TAG], True),
        (
            f"{commons.SKIP_FROM_STATS_NAME_MARKER} running",
            [commons.SKIP_FROM_STATS_TAG],
            True,
        ),
    ],
)
def test_activity_skip_from_stats(name: str, tags: list[str], expected: bool):
    # GIVEN
    activity = entities.ActivityEntity(name=name, tags=tags)

    # WHEN
    skip = activity.skip_from_stats

    # THEN
    assert skip is expected
    print("DONE")
