# Python Lab - AI Coding Agent Instructions

## Project Overview

This is a learning codebase containing multiple independent Python projects and exercises:

- **my_math/**: Custom implementations of mathematical functions (abs, trunc, floor, ceil, pow, sqrt, trig)
- **dsa_in_python/**: Data structures and algorithms implementations with multiple approaches
- **scrapers/**: Web scraping projects using requests, with CSV output and MySQL storage
- **recommender/**: Recommendation system algorithms
- **ultimate_25_days_DSA/**: Daily coding challenge solutions

## Testing Patterns

- Use `pytest` with `@pytest.mark.parametrize` for comprehensive test coverage
- Test against Python standard library functions (e.g., `math.abs`, `math.ceil`)
- Use `math.isclose()` for floating-point comparisons with `rel_tol=1e-9`
- Include edge cases: empty inputs, single elements, zeros, negatives, invalid types
- Test error handling with `pytest.raises(TypeError)` or `pytest.raises(ValueError)`
- Example from `tests/test_basic.py`:
  ```python
  @pytest.mark.parametrize("x", [0, 1, -1, 0.5, -0.5])
  def test_abs(x):
      assert my_abs(x) == abs(x)
  ```

## Code Implementation Patterns

- Functions include docstrings with Args/Returns sections
- Implement multiple algorithmic approaches for the same problem (e.g., `is_even` vs `is_even_bitwise`)
- Use try-except blocks with error printing for robustness
- Math functions should handle both int and float inputs
- Scrapers use hardcoded headers/cookies but store config in environment variables
- Database models use mysql-connector-python with connection pooling

## Error Handling

- Raise `TypeError` for invalid input types (not numeric)
- Raise `ValueError` for domain errors (e.g., `sqrt(-1)`)
- Avoid catching all exceptions generically; be specific

## Dependencies & Setup

- Dependencies listed in `installation.txt` files (e.g., `feedparser`, `mysql-connector-python`)
- Use `python-dotenv` for environment variable configuration
- Database config in separate `db_config.py` files
- Install with: `pip install -r installation.txt`

## Development Workflow

- Run tests: `pytest tests/test_*.py` or `pytest tests/test_basic.py -v`
- Implement stub functions (marked with `pass`) in math modules
- Fix failing tests by correcting algorithm implementations
- Add comprehensive test cases before implementing new features

## Key Reference Files

- `my_math/basic.py`: Core math function implementations
- `tests/test_basic.py`: Testing patterns and expected behavior
- `unsorted/scraper_vnnews/models/post.py`: Database model pattern
- `unsorted/dsa_in_python/chapter1/test_is_even.py`: Algorithm testing examples
