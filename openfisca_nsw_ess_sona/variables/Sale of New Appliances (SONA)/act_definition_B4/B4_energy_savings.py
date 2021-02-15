# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *


class B4_electricity_savings(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = 'What are the energy savings for the Implementation?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' Schedule C, Activity Definition C1.'

    def formula(buildings, period, parameters):
        star_rating = buildings('refrigerator_star_rating', period)  # this should be a parameter but it's not in a table in the Rule, pls advise
        refrigerator_volume = buildings('refrigerator_or_freezer_capacity', period)
        volume = select([refrigerator_volume < 200,
        refrigerator_volume >= 200 and refrigerator_volume < 250,
        refrigerator_volume >= 250],
        ["volume_less_than_200_litres", "volume_200_to_250_litres",
        "volume_over_250_litres"])
        deemed_equipment_electricity_savings = (parameters(period).SONA.table_B4_1.deemed_equipment_electricity_savings[star_rating][volume])
        return deemed_equipment_electricity_savings
