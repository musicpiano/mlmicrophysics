from numpy.distutils.core import setup, Extension
import subprocess
import os

ext_call_collect = Extension(name="mlmicrophysics.call_collect",
                             sources=["mlmicrophysics/call_collect.f90"],
                             extra_objects=["mlmicrophysics/stochastic_collect_tau_cam.o"])

with open("README.md", "r") as fh:
    long_description = fh.read()


if __name__ == "__main__":
    #fortran_compiler = "gfortran"
    #os.chdir("mlmicrophysics")
    #subprocess.call([fortran_compiler, "-c", "stochastic_collect_tau_cam.f90"])
    #os.chdir("../")
    setup(name="mlmicrophysics",
          version="0.1",
          description="Machine learning emulator testbed for microphysics.",
          long_description=long_description,
          long_description_content_type="text/markdown",
          author="David John Gagne and Gabrielle Gantos",
          author_email="dgagne@ucar.edu",
          license="MIT",
          url="https://github.com/NCAR/mlmicrophysics",
          packages=["mlmicrophysics"],
          #data_files=[("mlmicrophysics", ["mlmicrophysics/KBARF"])],
          install_requires=["numpy",
                            "scipy",
                            "pandas",
                            "matplotlib",
                            "xarray",
                            "tensorflow",
                            "netcdf4",
                            "scikit-learn",
                            "pyyaml",
                            "pyarrow"],
          #ext_modules=[ext_call_collect]
          )
