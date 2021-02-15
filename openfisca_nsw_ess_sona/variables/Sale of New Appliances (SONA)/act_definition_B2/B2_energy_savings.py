# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *


class B2_electricity_savings(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = 'What are the energy savings for the Implementation?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' Schedule C, Activity Definition C1.'

    def formula(buildings, period, parameters):
        star_rating = buildings('dryer_star_rating', period)  # this should be a parameter but it's not in a table in the Rule, pls advise
        machine_washing_load = buildings('B2_end_user_equipment_load', period)
        washing_load = select([machine_washing_load <= 5,
        machine_washing_load >= 5 and machine_washing_load < 8,
        machine_washing_load > 8],
        ["less_than_5kg", "between_5kg_and_8kg",
        "more_than_8kg"])
        deemed_equipment_electricity_savings = (parameters(period).SONA.table_B2_1.deemed_equipment_electricity_savings[star_rating][washing_load])
        return deemed_equipment_electricity_savings
