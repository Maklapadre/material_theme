import frappe
from frappe.custom.doctype.property_setter.property_setter import make_property_setter


DEFAULT_THEME_OPTIONS = ("Light", "Dark", "Automatic")
MATERIAL_THEME = "Material"


def execute():
	"""Register Material as a supported User desk theme using standard metadata."""
	current_options = frappe.db.get_value(
		"DocField",
		{"parent": "User", "fieldname": "desk_theme"},
		"options",
	) or ""
	theme_options = [option.strip() for option in current_options.splitlines() if option.strip()]

	if not theme_options:
		theme_options = list(DEFAULT_THEME_OPTIONS)
	if MATERIAL_THEME not in theme_options:
		theme_options.append(MATERIAL_THEME)

	make_property_setter(
		"User",
		"desk_theme",
		"options",
		"\n".join(theme_options),
		"Text",
	)
	frappe.clear_cache(doctype="User")
