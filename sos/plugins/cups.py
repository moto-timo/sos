# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from sos.plugins import Plugin, RedHatPlugin, DebianPlugin, UbuntuPlugin


class Cups(Plugin, RedHatPlugin, DebianPlugin, UbuntuPlugin):
    """CUPS IPP print service
    """

    plugin_name = 'cups'
    profiles = ('hardware',)

    packages = ('cups',)

    def setup(self):
        if not self.get_option("all_logs"):
            limit = self.get_option("log_size")
            self.add_copy_spec("/var/log/cups/access_log", sizelimit=limit)
            self.add_copy_spec("/var/log/cups/error_log", sizelimit=limit)
            self.add_copy_spec("/var/log/cups/page_log", sizelimit=limit)
        else:
            self.add_copy_spec("/var/log/cups")

        self.add_copy_spec([
            "/etc/cups/*.conf",
            "/etc/cups/*.types",
            "/etc/cups/lpoptions",
            "/etc/cups/ppd/*.ppd"
        ])

        self.add_cmd_output([
            "lpstat -t",
            "lpstat -s",
            "lpstat -d"
        ])

# vim: set et ts=4 sw=4 :
