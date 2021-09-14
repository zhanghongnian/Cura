# Copyright (c) 2021 Ultimaker B.V.
# Cura is released under the terms of the LGPLv3 or higher.

from typing import Any, Dict, TYPE_CHECKING

from . import VersionUpgrade411to412

if TYPE_CHECKING:
    from UM.Application import Application

upgrade = VersionUpgrade411to412.VersionUpgrade411to412()


def getMetaData() -> Dict[str, Any]:
    return {
        "version_upgrade": {
            # From                            To                                Upgrade function
            ("machine_stack",      5000017):  ("machine_stack",      5000018,   upgrade.upgradeStack),
            ("extruder_train",     5000017):  ("extruder_train",     5000018,   upgrade.upgradeStack),
            ("definition_changes", 4000017):  ("definition_changes", 4000018,   upgrade.upgradeInstanceContainer),
            ("quality_changes",    4000017):  ("quality_changes",    4000018,   upgrade.upgradeInstanceContainer),
            ("quality",            4000017):  ("quality",            4000018,   upgrade.upgradeInstanceContainer),
            ("user",               4000017):  ("user",               4000018,   upgrade.upgradeInstanceContainer),
            ("preferences",        7000017):  ("preferences",        7000018,   upgrade.upgradePreferences),
        },
        "sources": {
            "machine_stack": {
                "get_version": upgrade.getCfgVersion,
                "location": {"./machine_instances"}
            },
            "extruder_train": {
                "get_version": upgrade.getCfgVersion,
                "location": {"./extruders"}
            },
            "definition_changes": {
                "get_version": upgrade.getCfgVersion,
                "location": {"./definition_changes"}
            },
            "quality_changes": {
                "get_version": upgrade.getCfgVersion,
                "location": {"./quality_changes"}
            },
            "quality": {
                "get_version": upgrade.getCfgVersion,
                "location": {"./quality"}
            },
            "user": {
                "get_version": upgrade.getCfgVersion,
                "location": {"./user"}
            }
        }
    }


def register(app: "Application") -> Dict[str, Any]:
    return {"version_upgrade": upgrade}
