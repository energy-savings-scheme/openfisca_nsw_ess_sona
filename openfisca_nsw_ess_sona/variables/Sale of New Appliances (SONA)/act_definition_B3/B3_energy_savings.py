# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *


class B3_electricity_savings(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = 'What are the energy savings for the Implementation?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' Schedule C, Activity Definition C1.'

    def formula(buildings, period, parameters):
        star_rating = buildings('dishwasher_star_rating', period)  # this should be a parameter but it's not in a table in the Rule, pls advise
        number_of_place_settings = buildings('B3_number_of_place_settings', period)
        place_settings = select([number_of_place_settings < 9,
        number_of_place_settings >= 9 and number_of_place_settings < 13,
        number_of_place_settings >= 13],
        ["less_than_nine_place_settings", "nine_to_thirteen_place_settings",
        "over_thirteen_place_settings"])
        deemed_equipment_electricity_savings = (parameters(period).SONA.table_B3_1.deemed_equipment_electricity_savings[star_rating][place_settings])
        return deemed_equipment_electricity_savings
