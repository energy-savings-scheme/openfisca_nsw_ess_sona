# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *


class B5_electricity_savings(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = 'What are the energy savings for the Implementation?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' Schedule C, Activity Definition C1.'

    def formula(buildings, period, parameters):
        star_rating = buildings('refrigerator_star_rating', period)  # this should be a parameter but it's not in a table in the Rule, pls advise
        refrigerator_volume = buildings('refrigerator_or_freezer_capacity', period)
        volume = select([refrigerator_volume < 300,
        refrigerator_volume >= 300 and refrigerator_volume < 450,
        refrigerator_volume >= 450 and refrigerator_volume < 550,
        refrigerator_volume >= 550],
        ["volume_less_than_300_litres", "volume_300_to_450_litres",
        "volume_450_to_550_litres", "volume_550_litres_or_over"])
        deemed_equipment_electricity_savings = (parameters(period).SONA.table_B5_1.deemed_equipment_electricity_savings[star_rating][volume])
        return deemed_equipment_electricity_savings


class B5_energy_savings(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = 'What are the energy savings for the Implementation, if eligible?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' Schedule C, Activity Definition C1.'

    def formula(buildings, period, parameters):
        elec_savings = buildings('B5_electricity_savings', period)
        is_eligible = buildings('B5_meets_all_equipment_requirements', period)
        return elec_savings * is_eligible
