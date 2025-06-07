from dataclasses import dataclass

@dataclass(frozen=True)
class Layout:
    page: str = "min-h-screen bg-gray-50"
    container: str = "max-w-2xl mx-auto p-6"
    header: str = "flex items-center justify-between mb-6"
    task_item: str = "flex items-center justify-between py-2"
    form_group: str = "space-y-2"
    task_list: str = "mt-6 space-y-2"
    content_card: str = "bg-white p-6 rounded-lg shadow-md"

@dataclass(frozen=True)
class Typography:
    heading: str = "text-3xl font-bold text-gray-800 mb-6"
    text: str = "text-gray-700"
    text_with_margin: str = "text-gray-700 mb-4"
    text_semibold: str = "text-gray-700 font-semibold mb-2"
    text_muted: str = "text-gray-600 mb-1"
    text_small: str = "text-sm"

@dataclass(frozen=True)
class Buttons:
    primary: str = "px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
    primary_with_margin: str = "mt-2 px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
    primary_inline: str = "inline-block px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
    delete: str = "ml-2 px-2 py-1 text-sm text-red-600 hover:text-red-800 hover:bg-red-100 rounded"

@dataclass(frozen=True)
class Forms:
    input: str = "w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"

@dataclass(frozen=True)
class Components:
    task_item: str = "border-b border-gray-200"
    list: str = "list-disc list-inside ml-4 mb-6"

@dataclass(frozen=True)
class Links:
    nav: str = "text-blue-500 hover:text-blue-700 text-sm"

# Create instances for easy access
layout = Layout()
typography = Typography()
buttons = Buttons()
forms = Forms()
components = Components()
links = Links() 