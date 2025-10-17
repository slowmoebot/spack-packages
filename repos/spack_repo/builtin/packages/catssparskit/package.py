# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install sparskit
#
# You can edit this file again by typing:
#
#     spack edit sparskit
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class Catssparskit(CMakePackage):
    """Copy of Sparskit but with cmake"""

    homepage = "https://www.example.com"
    git = "cats-git:sparskit"

    version("main", branch="main")

    depends_on("fortran", type="build")
    depends_on("c", type="build")

    @run_after("install")
    def fixup_install(self):

        # Make dummy include directory since spack will look for it and fail otherwise
        mkdirp(prefix.include)
