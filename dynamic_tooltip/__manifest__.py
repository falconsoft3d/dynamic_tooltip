# coding: utf-8
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2017 Marlon Falcón Hernandez
#    (<http://www.falconsolutions.cl>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Dynamic Tooltip MFH',
    'version': '10.0.1.0.0',
    'author': 'Falcon Solutions SpA',
    'maintainer': 'Falcon Solutions',
    'website': 'http://www.falconsolutions.cl',
    'license': 'AGPL-3',
    'category': 'Tools',
    'summary': u'Widget para mostrar información extra',
    'description': u"""Agrega un ícono a un campo de la vista, que al pasar el
    mouse sobre el mismo mostrará información dinámicamente """,
    'depends': [],
    'data': ['tooltip.xml'],
    'installable': True,
    'application': True,
    'demo': [],
    'test': []
}
