# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *


class B1_end_user_equipment_is_clothes_washing_machine(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Is the new End User Equipment a Clothes Washing Machine?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' Schedule B, Activity Definition B1, Equipment Requirement 1.'


class B1_end_user_equipment_is_labelled_for_energy_labelling(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Is the new End User Equipment registered for energy labelling?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' Schedule B, Activity Definition B1, Equipment Requirement 2.'


class WashingMachineStarRating(Enum):
    zero_stars = 'Washing machine is rated at zero stars.'
    one_star = 'Washing machine is rated at one star.'
    one_and_a_half_star = 'Washing machine is rated at one and a half star.'
    two_stars = 'Washing machine is rated at two stars.'
    two_and_a_half_stars = 'Washing machine is rated at two and a half stars.'
    three_stars = 'Washing machine is rated at three stars.'
    three_and_a_half_stars = 'Washing machine is rated at three and a half stars.'
    four_stars = 'Washing machine is rated at four stars.'
    four_and_a_half_stars = 'Washing machine is rated at four and a half stars.'
    five_stars = 'Washing machine is rated at five stars.'
    five_and_a_half_stars = 'Washing machine is rated at five and a half stars.'
    six_stars = 'Washing machine is rated at six stars.'

class washing_machine_star_rating(Variable):
    value_type = Enum # note need to recode as Enum once reading AS2040
    entity = Building
    possible_values = WashingMachineStarRating
    default_value = WashingMachineStarRating.zero_stars
    definition_period = ETERNITY
    label = 'What is the star rating for the clothes washing machine, as' \
            ' rated in GEMS?'
    #  need to put in what activities this is relevant for


class B1_end_user_equipment_is_top_or_front_loader(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Is the new End User Equipment a top loader or a front loader?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' Schedule B, Activity Definition B1, Equipment Requirement 3.'
                # change to enum when you get chance

    def formula(buildings, period, parameters):
        is_top_loader = buildings('B1_end_user_equipment_is_top_loader', period)
        is_front_loader = buildings('B1_end_user_equipment_is_front_loader', period)
        return is_top_loader + is_front_loader


class B1_end_user_equipment_is_top_loader(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Is the new End User Equipment a top loader or a front loader?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' Schedule B, Activity Definition B1, Equipment Requirement 3.'


class B1_end_user_equipment_is_front_loader(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Is the new End User Equipment a top loader or a front loader?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' Schedule B, Activity Definition B1, Equipment Requirement 3.'


class B1_end_user_equipment_has_a_load(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Does the new End User Equipment has a load, as recorded in the' \
            ' GEMS Registry?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' Schedule B, Activity Definition B1, Equipment Requirement 4.'

    def formula(buildings, period, parameters):
        equipment_load = buildings('B1_end_user_equipment_load', period)
        condition_has_load = (equipment_load != 0 and equipment_load is not None)
        return condition_has_load


class B1_end_user_equipment_load(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = 'What is the equipment load of the new end user equipment, in kilograms?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' Schedule B, Activity Definition B1, Equipment Requirement 4.'


class B1_end_user_equipment_is_combination_washer_dryer(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Is the new End User Equipment a combination washer/dryer?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' Schedule B, Activity Definition B1, Equipment Requirement 5.'


class B1_meets_all_equipment_requirements(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Does the new End User Equipment meet all of the Equipment' \
            ' Requirements detailed in Activity Definition B1?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' Schedule B, Activity Definition B1.'

    def formula(buildings, period, parameters):
        is_clothes_washing_machine = buildings('B1_end_user_equipment_is_clothes_washing_machine', period)
        is_labelled_for_energy_labelling = buildings('B1_end_user_equipment_is_labelled_for_energy_labelling', period)
        is_top_or_front_loader = buildings('B1_end_user_equipment_is_top_or_front_loader', period)
        has_load = buildings('B1_end_user_equipment_has_a_load', period)
        return (is_clothes_washing_machine * is_labelled_for_energy_labelling
        * is_top_or_front_loader * has_load)
