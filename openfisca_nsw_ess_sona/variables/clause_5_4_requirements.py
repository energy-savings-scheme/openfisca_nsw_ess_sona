# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *


class installed_ineligible_end_equipment(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = 'Equation 1 of the ESS Rule 2009, used to calculate the number' \
            ' of ESCs generated from a Recognised Energy Savings Activity.' \
            ' As defined in Clause 6.5 of the ESS Rule 2009.'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' clause 5.4 (a) (i) - Activities which are not Recognised' \
                ' Energy Saving Activities.'

    def formula(buildings, period, parameters):
        T5_adaptor_kits_are_ineligible = buildings('T5_adaptor_kits_are_ineligible', period)
        retrofit_LED_linear_lamps_are_ineligible = buildings('retrofit_LED_linear_lamps_are_ineligible', period)
        return T5_adaptor_kits_are_ineligible + retrofit_LED_linear_lamps_are_ineligible


class T5_adaptor_kits_are_ineligible(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Is the new End User Equipment a T5 Adaptor Kit, as defined' \
            ' in Table A9.3? T5 Adaptor Kits are not eligible to create ESCs.'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' clause 5.4 (a) (i) - Activities which are not Recognised' \
                ' Energy Saving Activities.'

    def formula(buildings, period, parameters):
        new_lamp_type = buildings('new_lamp_type', period)
        EquipmentClassStatus = new_lamp_type.possible_values  # imports functionality of Table A9.1 and Table A9.3 to define existing lamp type
        is_T5_adaptor_kit = (new_lamp_type == EquipmentClassStatus.T5_adaptor_kit)
        return is_T5_adaptor_kit


class retrofit_LED_linear_lamps_are_ineligible(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Is the new End User Equipment a Retrofit Luminaire LED Linear' \
            ' Lamp, as defined in Table A9.3? Retrofit Luminaire LED Linear' \
            ' Lamps are not eligible to create ESCs.'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' clause 5.4 (a) (ii) - Activities which are not Recognised' \
                ' Energy Saving Activities.'

    def formula(buildings, period, parameters):
        new_lamp_type = buildings('new_lamp_type', period)
        EquipmentClassStatus = new_lamp_type.possible_values  # imports functionality of Table A9.1 and Table A9.3 to define existing lamp type
        is_LED_linear_lamp = (new_lamp_type == EquipmentClassStatus.retrofit_luminaire_LED_linear_lamp)
        return is_LED_linear_lamp


class activity_required_to_comply_with_mandatory_legal_requirements(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Is the activity undertaken to comply with a mandatory legal' \
            ' requirement imposed through a statutory or regulatory instrument' \
            ' of any jurisdiction, including BASIX and BCA requirements?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' clause 5.4 (b) - Activities which are not Recognised' \
                ' Energy Saving Activities.'


class activity_is_standard_control_service_or_prescribed_transmission_service(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Is the activity a Standard Control Service or a Prescribed' \
            ' Transmission Service undertaken by a Network Service Provider?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' clause 5.4 (c) - Activities which are not Recognised' \
                ' Energy Saving Activities.'


class activity_is_supply_purchase_from_retailer_for_emissions_reduction(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Is the activity a purchase or supply of electricity from a retailer' \
            ' with a representation that the purchased or supplied electricity' \
            ' reduces greenhouse emissions?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' clause 5.4 (d) - Activities which are not Recognised' \
                ' Energy Saving Activities.'


class production_or_service_levels_are_reduced(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Does the activity result in a reduction of the consumption of' \
            ' energy by reducing production levels, service levels, or both?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' clause 5.4 (e) - Activities which are not Recognised' \
                ' Energy Saving Activities.'  # Note duplication w. 5.3 (b)

    def formula(buildings, period, parameters):
        reduces_production_or_service_levels = buildings('activity_reduces_production_or_service_levels', period)
        return reduces_production_or_service_levels


class increases_non_renewable_fuel_consumption_for_equivalent_services(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Does the activity reduce energy consumption by increasing' \
            ' consumption of non-renewable fuels, other than Gas, to provide' \
            ' equivalent goods or services?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' clause 5.4 (f) - Activities which are not Recognised' \
                ' Energy Saving Activities.'


class is_eligible_to_create_RECs(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Is the activity eligible to create certificates under the' \
            ' Renewable Energy (Electricity) Act 2000?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' clause 5.4 (g) - Activities which are not Recognised' \
                ' Energy Saving Activities.'


class activity_flares_gas(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Does the activity result in the flaring of Gas?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' clause 5.4 (h) - Activities which are not Recognised' \
                ' Energy Saving Activities.'


class activity_exports_to_the_electricity_network(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Does the activity result in generating electricity which is' \
            ' exported to the Electricity Network?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' clause 5.4 (i) (i) - Activities which are not Recognised' \
                ' Energy Saving Activities.'


class generating_system_more_than_30MW(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Does the generating system have a nameplate rating of 30MW or higher?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' clause 5.4 (i) (ii) - Activities which are not Recognised' \
                ' Energy Saving Activities.'

    def formula(buildings, period, parameters):
        nameplate_rating = buildings('generator_nameplate_rating', period)
        return nameplate_rating >= 30


class generator_nameplate_rating(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = 'What is the nameplate rating of the generating system, in MW?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' clause 5.4 (i) (ii) - Activities which are not Recognised' \
                ' Energy Saving Activities.'


class baseline_greenhouse_gas_emissions(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = 'What are the greenhouse gas emissions prior to the commencement' \
            ' of a fuel switching activity?'  # need to determine if this is an annual, monthly, daily measurement
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' clause 5.4 (j) - Activities which are not Recognised' \
                ' Energy Saving Activities.'


class current_greenhouse_gas_emissions(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = 'What are the greenhouse gas emissions following the completion' \
            ' of a fuel switching activity?'  # need to determine if this is an annual, monthly, daily measurement
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' clause 5.4 (j) - Activities which are not Recognised' \
                ' Energy Saving Activities.'


class fuel_switching_activity_leads_to_greenhouse_emissions_increase(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Does the fuel switching activity, implemented under clause 7A' \
            ' , 8.5, 8.6 or 8.7 lead to a net increase in greenhouse gas' \
            ' emissions'  # need to determine if this is an annual, monthly, daily measurement
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' clause 5.4 (j) - Activities which are not Recognised' \
                ' Energy Saving Activities.'

    def formula(buildings, period, parameters):
        is_fuel_switching = buildings('is_fuel_switching_activity', period)
        baseline_emissions = buildings('baseline_greenhouse_gas_emissions', period)
        current_emissions = buildings('current_greenhouse_gas_emissions', period)
        return (is_fuel_switching * (current_emissions > baseline_emissions)) + (not(is_fuel_switching))


class in_ACT_and_required_to_report_under_national_schemes(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Is the activity required to report energy consumption under the' \
            ' National Greenhouse and Energy Reporting Act 2007?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' clause 5.4 (j) - Activities which are not Recognised' \
                ' Energy Saving Activities.'

    def formula(buildings, period, parameters):
        state = buildings('implementation_state', period)
        ImplementationState = state.possible_values
        in_ACT = (state == ImplementationState.ACT)
        national_greenhouse_act = buildings('required_to_report_under_national_greenhouse_act', period)
        EE_in_govt_operations = buildings('required_to_report_under_energy_efficiency_in_government_operations_policy', period)
        carbon_neutral_framework = buildings('required_to_report_under_carbon_neutral_ACT_government_framework', period)
        return (in_ACT * (national_greenhouse_act + EE_in_govt_operations + carbon_neutral_framework))


class required_to_report_under_national_greenhouse_act(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Is the activity required to report energy consumption under the' \
            ' National Greenhouse and Energy Reporting Act 2007?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' clause 5.4 (k) (i) - Activities which are not Recognised' \
                ' Energy Saving Activities.'


class required_to_report_under_energy_efficiency_in_government_operations_policy(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Is the activity required to report energy consumption under the' \
            ' Energy Efficiency in Government Operations Policy?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' clause 5.4 (k) (ii) - Activities which are not Recognised' \
                ' Energy Saving Activities.'


class required_to_report_under_carbon_neutral_ACT_government_framework(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Is the activity required to report energy consumption under the' \
            ' Energy Efficiency in Government Operations Policy?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' clause 5.4 (k) (iii) - Activities which are not Recognised' \
                ' Energy Saving Activities.'


class ACT_lighting_upgrade_as_part_of_development(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Is the activity a. in the ACT, b. a Lighting Upgrade, and c.' \
            ' undertaken as part of a development or refurbishment requiring' \
            ' development approval, under the Planning and Development Act 2007?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' clause 5.4 (l) - Activities which are not Recognised' \
                ' Energy Saving Activities.'  # need to remember to code in logic for it being a Lighting Upgrade

    def formula(buildings, period, parameters):
        state = buildings('implementation_state', period)
        ImplementationState = state.possible_values
        in_ACT = (state == ImplementationState.ACT)  # need to code in activity type Enum
        activity_undertaken_as_part_of_development = buildings('activity_undertaken_as_part_of_development', period)
        activity_undertaken_as_part_of_refurbishment = buildings('activity_undertaken_as_part_of_refurbishment_requiring_development_approval', period)
        return (in_ACT * (activity_undertaken_as_part_of_development + activity_undertaken_as_part_of_refurbishment))


class activity_undertaken_as_part_of_development(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Is the activity undertaken as part of a development under the' \
            ' Planning and Development Act?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' clause 5.4 (l) - Activities which are not Recognised' \
                ' Energy Saving Activities.'


class activity_undertaken_as_part_of_refurbishment_requiring_development_approval(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Is the activity undertaken as part of a refurbishment requiring' \
            ' development approval under the Planning and Development Act?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' clause 5.4 (l) - Activities which are not Recognised' \
                ' Energy Saving Activities.'


class activity_is_ineligible_for_RESA_criteria(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Does the activity meet any of the criteria which makes it' \
            ' ineligible to be considered a RESA?'
    reference = 'Energy Savings Scheme Rule of 2009, Effective 30 March 2020,' \
                ' clause 5.4 - Activities which are not Recognised' \
                ' Energy Saving Activities.'

    def formula(buildings, period, parameters):
        state = buildings('implementation_state', period)
        ImplementationState = state.possible_values
        in_ACT = (state == ImplementationState.ACT)
        in_NSW = (state == ImplementationState.NSW)
        not_in_ACT_or_NSW = (state != ImplementationState.ACT and state != ImplementationState.NSW)
        installed_ineligible_end_equipment = buildings('installed_ineligible_end_equipment', period)
        activity_complies_with_mandatory_legal_requirement = buildings('activity_required_to_comply_with_mandatory_legal_requirements', period)
        control_or_transmission_service = buildings('activity_is_standard_control_service_or_prescribed_transmission_service', period)
        supply_or_purchase_for_greenhouse_reductions = buildings('activity_is_supply_purchase_from_retailer_for_emissions_reduction', period)
        production_or_service_levels_are_reduced = buildings('production_or_service_levels_are_reduced', period)
        increases_non_renewable_fuel_consumption = buildings('increases_non_renewable_fuel_consumption_for_equivalent_services', period)
        eligible_to_create_RECs = buildings('is_eligible_to_create_RECs', period)
        activity_flares_gas = buildings('activity_flares_gas', period)
        activity_exports_to_the_electricity_network = buildings('activity_exports_to_the_electricity_network', period)
        generating_system_more_than_30MW = buildings('generating_system_more_than_30MW', period)
        fuel_switching_leads_to_increased_greenhouse_emissions = buildings('fuel_switching_activity_leads_to_greenhouse_emissions_increase', period)
        in_ACT_and_required_to_report_under_national_schemes = buildings('in_ACT_and_required_to_report_under_national_schemes', period)
        ACT_lighting_upgrade_as_part_of_development = buildings('ACT_lighting_upgrade_as_part_of_development', period)
        return select([in_ACT, in_NSW, not_in_ACT_or_NSW],
                    [(installed_ineligible_end_equipment + activity_complies_with_mandatory_legal_requirement
                    + control_or_transmission_service + supply_or_purchase_for_greenhouse_reductions
                    + production_or_service_levels_are_reduced + increases_non_renewable_fuel_consumption
                    + eligible_to_create_RECs + activity_flares_gas + activity_exports_to_the_electricity_network
                    + generating_system_more_than_30MW + fuel_switching_leads_to_increased_greenhouse_emissions
                    + in_ACT_and_required_to_report_under_national_schemes + ACT_lighting_upgrade_as_part_of_development),
                    (installed_ineligible_end_equipment + activity_complies_with_mandatory_legal_requirement
                    + control_or_transmission_service + supply_or_purchase_for_greenhouse_reductions
                    + production_or_service_levels_are_reduced + increases_non_renewable_fuel_consumption
                    + eligible_to_create_RECs + activity_flares_gas + activity_exports_to_the_electricity_network
                    + generating_system_more_than_30MW + fuel_switching_leads_to_increased_greenhouse_emissions),
                    True])

#  first select pulls in ACT specific requirements, second select pulls in \
#  NSW specific requirements, third select returns ineligible because only \
#  NSW and ACT are within the ESS Jurisdiction (i.e. when outside of NSW and ACT, \
#  the user is ineligible to create ESC no matter the response to other requirements.)
