from behave import given, then, when
from cucumber_expressions.parameter_type import ParameterType

from environment import parameter_registry

# Define the parameter type
color_parameter = ParameterType(
    name="color",
    regexp="red|blue|yellow",
    type=str,
    transformer=lambda s: s,
    use_for_snippets=True,
    prefer_for_regexp_match=False,
)

# Pass the parameter type to the registry instance
parameter_registry.define_parameter_type(color_parameter)

@given("I am on the profile customisation/settings page")
def step_given(context):
    assert True


# Reference the parameter type in the step definition pattern
@when('I select the theme colo(u)r "{color}"')
def step_when(context, selected_color):
    assert selected_color
    context.selected_color = selected_color


@then('the profile colo(u)r should be "{color}"')
def step_then(context, displayed_color):
    assert displayed_color
    assert context.selected_color == displayed_color
