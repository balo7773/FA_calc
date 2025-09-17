# COMPANY_CUSTOM_METRIC_RULES.md

## Rules for Implementing the `custom_metric` Class Method in `Company`

### 1. PEP8 Compliance
- All code must strictly follow PEP8 style guidelines for readability and consistency.

### 2. Docstring Requirements
- Every method, especially `custom_metric`, must have a clear, descriptive docstring.
- Docstrings should explain the method's purpose, arguments, return values, exceptions, and any important details.

### 3. Inline Comments
- Inline comments are required for all non-trivial or complex code sections.
- Comments should clarify logic, especially for formula parsing and validation.

### 4. Input Validation
- Only numeric values and allowed variable names (matching financial parameters) should be accepted in formulas.
- Formulas must follow BODMAS (operator precedence) rules.
- Disallow functions, imports, or any code execution outside basic arithmetic (+, -, *, /, **, parentheses).
- Reject formulas containing unsupported or unsafe operations.

### 5. Formula Scope
- Only simple arithmetic formulas are allowed (no trigonometric, logarithmic, or statistical functions).
- If a user attempts a complex or unsupported formula, raise a clear error message.

### 6. Security
- Never use Python's `eval()` directly. Use a safe expression evaluator (e.g., `simpleeval`, `asteval`, or custom parser) that restricts execution to math and whitelisted variables.
- Validate formulas before evaluation to prevent code injection or denial of service.

### 7. Testing Practices
- Write unit tests for the `custom_metric` method covering valid, invalid, and edge-case formulas.
- Test for correct calculation, error handling, and security (e.g., attempts to inject code).

### 8. Suggestions for Extension
- Consider supporting basic math functions (abs, min, max) in the future, but only after thorough validation.
- Provide users with a list of available variables and example formulas.
- Allow users to edit or delete custom metrics in future versions.

---

**Note:** These rules apply only to the `custom_metric` method in the `Company` class. For broader codebase rules, see the main project guidelines.
