# lib/sql_queries.py

select_all_female_bears_return_name_and_age = """
    SELECT name, age
    FROM bears
    WHERE sex = 'F';
"""

select_all_bears_names_and_ages_ordered_by_age = """
    SELECT name, age
    FROM bears
    ORDER BY age ASC;
"""

select_oldest_bear_and_returns_name_and_age = """
    SELECT name, age
    FROM bears
    ORDER BY age DESC
    LIMIT 1;
"""

select_youngest_bear_and_returns_name_and_age = """
    SELECT name, age
    FROM bears
    ORDER BY age ASC
    LIMIT 1;
"""

select_bear_with_null_name = """
    SELECT *
    FROM bears
    WHERE name IS NULL;
"""

select_bear_with_name_not_null = """
    SELECT *
    FROM bears
    WHERE name IS NOT NULL;
"""

select_all_bears_ordered_by_temperament = """
    SELECT *
    FROM bears
    ORDER BY temperament ASC;
"""
