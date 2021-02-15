# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *


class B3_end_user_equipment_is_dishwasher(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Is the new End User Equipment a Dishwasher?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' Schedule B, Activity Definition B3, Equipment Requirement 1.'


class B3_end_user_equipment_is_labelled_for_energy_labelling(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Is the new End User Equipment registered for energy labelling?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' Schedule B, Activity Definition B3, Equipment Requirement 2.'


class DishwasherStarRating(Enum):
    zero_stars = 'Dishwasher is rated at zero stars.'
    one_star = 'Dishwasher is rated at one star.'
    one_and_a_half_star = 'Dishwasher is rated at one and a half star.'
    two_stars = 'Dishwasher is rated at two stars.'
    two_and_a_half_stars = 'Dishwasher is rated at two and a half stars.'
    three_stars = 'Dishwasher is rated at three stars.'
    three_and_a_half_stars = 'Dishwasher is rated at three and a half stars.'
    four_stars = 'Dishwasher is rated at four stars.'
    four_and_a_half_stars = 'Dishwasher is rated at four and a half stars.'
    five_stars = 'Dishwasher is rated at five stars.'
    five_and_a_half_stars = 'Dishwasher is rated at five and a half stars.'
    six_stars = 'Dishwasher is rated at six stars.'
    seven_stars = 'Dishwasher is rated at seven stars.'
    eight_stars = 'Dishwasher is rated at eight stars.'
    nine_stars = 'Dishwasher is rated at nine stars.'
    ten_stars = 'Dishwasher is rated at ten stars.'

class dishwasher_star_rating(Variable):
    value_type = Enum
    possible_values = DishwasherStarRating
    default_value = DishwasherStarRating.zero_stars
    entity = Building
    definition_period = ETERNITY
    label = 'What is the star rating for the dishwasher, as' \
            ' rated in GEMS?'
    # for use in Activity Definition B3.


class B3_end_user_equipment_has_registered_place_settings(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Does the new End User Equipment have a number of place settings,' \
            ' recorded in the GEMS Registry?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' Schedule B, Activity Definition B3, Equipment Requirement 3.'

    def formula(buildings, period, parameters):
        place_settings = buildings('B3_number_of_place_settings', period)
        condition_has_place_settings = (place_settings != 0 and place_settings is not None)
        return condition_has_place_settings


class B3_number_of_place_settings(Variable):
    value_type = int
    entity = Building
    definition_period = ETERNITY
    label = 'What is the number of place settings in the new End User Equipment?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' Schedule B, Activity Definition B3, Equipment Requirement 3.'


class B3_meets_all_equipment_requirements(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Does the new End User Equipment meet all of the Equipment' \
            ' Requirements detailed in Activity Definition B1?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' Schedule B, Activity Definition B1.'

    def formula(buildings, period, parameters):
        is_dishwasher = buildings('B3_end_user_equipment_is_dishwasher', period)
        is_labelled_for_energy_labelling = buildings('B3_end_user_equipment_is_labelled_for_energy_labelling', period)
        has_place_settings = buildings('B3_end_user_equipment_has_registered_place_settings', period)
        return (is_dishwasher * is_labelled_for_energy_labelling * has_place_settings)
