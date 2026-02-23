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
#     spack install decompose
#
# You can edit this file again by typing:
#
#     spack edit decompose
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Decompose(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://git.rwth-aachen.de/cats-gitolite/private/tools/decompose"
    git = "git@git.rwth-aachen.de:cats-gitolite/private/tools/decompose.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    # FIXME: Add proper versions and checksums here.
    # version("1.2.3", md5="0123456789abcdef0123456789abcdef")


    variant("scotch", default=False, description="Use Scotch for graph partitioning")
    variant("metis", default=True, description="Use Metis for graph partitioning")

    # FIXME: Add dependencies if required.
    depends_on("cxx", type="build")
    depends_on("c", type="build")
    depends_on("mixdclass")
    depends_on("boost+program_options")
    depends_on("mpi")
    depends_on("scotch", when="+scotch")
    depends_on("parmetis", when="+metis")

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = [
            self.define("CMAKE_C_COMPILER", self.spec["mpi"].mpicc),
            self.define("CMAKE_CXX_COMPILER", self.spec["mpi"].mpicxx),
            self.define("CMAKE_Fortran_COMPILER", self.spec["mpi"].mpifc),
        ]
        return args
