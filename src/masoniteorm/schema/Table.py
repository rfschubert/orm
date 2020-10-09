from .Column import Column
from .Constraint import Constraint
from .Index import Index
from .ForeignKeyConstraint import ForeignKeyConstraint


class Table:
    def __init__(self, table):
        self.name = table
        self.added_columns = {}
        self.added_constraints = {}
        self.added_indexes = {}
        self.added_foreign_keys = {}
        self.renamed_columns = {}
        self.drop_indexes = {}
        self.foreign_keys = {}
        self.primary_key = None

    def add_column(
        self, name=None, column_type=None, length=None, nullable=False, default=None
    ):
        self.added_columns.update({name: Column(name, column_type)})
        return self

    def add_constraint(self, name, constraint_type, columns=[]):
        self.added_constraints.update(
            {name: Constraint(name, constraint_type, columns=columns)}
        )

    def add_foreign_key(self, column, table, foreign_column):
        self.added_foreign_keys.update(
            {column: ForeignKeyConstraint(column, table, foreign_column)}
        )

    def get_added_foreign_keys(self):
        return self.added_foreign_keys

    def get_constraint(self, name):
        return self.added_constraints[name]

    def get_added_constraints(self):
        return self.added_constraints

    def get_added_columns(self):
        return self.added_columns

    def rename_column(self, column, to):
        pass

    def set_primary_key(self, key):
        self.primary_key = key
        self.added_columns[key].set_as_primary()
        return self

    def add_index(self, name, index_type):
        self.added_indexes.update({name: Index(name, index_type)})

    def get_index(self, name):
        return self.added_indexes[name]

    def drop_index(self, index):
        pass
