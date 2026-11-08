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


@pytest.mark.mytral
@pytest.mark.parametrize(
    "activity_type_key, expected",
    [
        (commons.AT_RUN, 1.0),
        (commons.AT_RUN_TRAIL, 1.0),
        (commons.AT_RIDE, 0.33),
        (commons.AT_RIDE_MOUNTAIN, 0.4),
        (commons.AT_RIDE_GRAVEL, 0.33),
        (commons.AT_RIDE_VIRTUAL, 0.33),
        (commons.AT_ROW, 1.0),
        (commons.AT_ROW_ERG, 1.0),
        (commons.AT_SKI_F, 0.5),
        (commons.AT_RS_DP, 0.5),
        (commons.AT_SKI_BACKCOUNTRY, 0.5),
        (commons.AT_SWIM, 5.0),
        (commons.AT_HIKE, 0.8),
        (commons.AT_WALK, 0.8),
        (commons.AT_KAYAK, commons.UKM_COEFFICIENT_NOT_COUNTED),
        (commons.AT_SKI_DOWNHILL, commons.UKM_COEFFICIENT_NOT_COUNTED),
        ("unknown-activity-type", commons.UKM_COEFFICIENT_NOT_COUNTED),
    ],
)
def test_ukm_coefficient(activity_type_key: str, expected: float):
    # GIVEN
    # parametrized activity type key and legacy coefficients (active)

    # WHEN
    coefficient = commons.ukm_coefficient(activity_type_key)

    # THEN
    assert coefficient == expected
    print("DONE")
