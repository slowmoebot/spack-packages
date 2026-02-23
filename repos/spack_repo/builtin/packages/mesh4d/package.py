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
#     spack install mesh4d
#
# You can edit this file again by typing:
#
#     spack edit mesh4d
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Mesh4d(MakefilePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://git.rwth-aachen.de/cats-gitolite/private/tools/mesh4d"
    git = "git@git.rwth-aachen.de:cats-gitolite/private/tools/mesh4d.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    # FIXME: Add dependencies if required.
    # depends_on("foo")

    depends_on("c", type="build")
    depends_on("fortran", type="build")
    depends_on('qhull')
    depends_on('lapack')
    depends_on('ewd~mpi')

    def setup_build_environment(self, env):
        # Set hosttype based on compiler
        print(f"Setting up build environment for compiler: {self.spec.compiler.name}")
        if self.spec.compiler.name == "intel":
            env.set("HOSTTYPE", "rzbull")
        else:
            env.set("HOSTTYPE", "rzbullGcc")
        

        # Set library paths
        env.set("qhull_lib", str(self.spec["qhull"].prefix.lib))
        env.set("ewd_lib", str(self.spec["ewd"].prefix.lib))
