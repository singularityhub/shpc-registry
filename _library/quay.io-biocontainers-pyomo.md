---
layout: container
name:  "quay.io/biocontainers/pyomo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pyomo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pyomo/container.yaml"
updated_at: "2022-11-07 00:53:52.518058"
latest: "4.1.10527--py34_0"
container_url: "https://biocontainers.pro/tools/pyomo"
aliases:
 - "2to3-3.4"
 - "OSSolverService"
 - "PyomoOSSolverService"
 - "checkCopyright"
 - "checkcopyright"
 - "computeconf"
 - "dispatch_srvr"
 - "easy_install-3.4"
 - "idle3.4"
 - "kill_pyro_mip_servers"
 - "launch_pyro_mip_servers"
 - "lbin"
 - "lpython"
 - "phsolverserver"
 - "pydoc3.4"
 - "pyomo"
 - "pyomo_ns"
 - "pyomo_nsc"
 - "pyomo_old"
 - "pyomo_python"
 - "pypi_downloads"
 - "pyro_mip_server"
 - "python3.4"
 - "python3.4-config"
 - "python3.4m"
 - "python3.4m-config"
 - "pyutilib_test_driver"
 - "pyvenv-3.4"
 - "readsol"
 - "replaceCopyright"
 - "replacecopyright"
 - "results_schema"
 - "runbenders"
 - "runef"
 - "runph"
 - "test.pyomo"
 - "test.pyutilib"
 - "nosetests"
 - "tclsh8.5"
 - "wish8.5"
 - "ncurses5-config"
 - "ncursesw5-config"
 - "pyvenv"
versions:
 - "4.1.10527--py34_0"
description: "shpc-registry automated BioContainers addition for pyomo"
config: {"url": "https://biocontainers.pro/tools/pyomo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pyomo", "latest": {"4.1.10527--py34_0": "sha256:8b83739f4216ebadb1f720eb773a079c9a7ceb12763783268472e4502dc87d28"}, "tags": {"4.1.10527--py34_0": "sha256:8b83739f4216ebadb1f720eb773a079c9a7ceb12763783268472e4502dc87d28"}, "docker": "quay.io/biocontainers/pyomo", "aliases": {"2to3-3.4": "/usr/local/bin/2to3-3.4", "OSSolverService": "/usr/local/bin/OSSolverService", "PyomoOSSolverService": "/usr/local/bin/PyomoOSSolverService", "checkCopyright": "/usr/local/bin/checkCopyright", "checkcopyright": "/usr/local/bin/checkcopyright", "computeconf": "/usr/local/bin/computeconf", "dispatch_srvr": "/usr/local/bin/dispatch_srvr", "easy_install-3.4": "/usr/local/bin/easy_install-3.4", "idle3.4": "/usr/local/bin/idle3.4", "kill_pyro_mip_servers": "/usr/local/bin/kill_pyro_mip_servers", "launch_pyro_mip_servers": "/usr/local/bin/launch_pyro_mip_servers", "lbin": "/usr/local/bin/lbin", "lpython": "/usr/local/bin/lpython", "phsolverserver": "/usr/local/bin/phsolverserver", "pydoc3.4": "/usr/local/bin/pydoc3.4", "pyomo": "/usr/local/bin/pyomo", "pyomo_ns": "/usr/local/bin/pyomo_ns", "pyomo_nsc": "/usr/local/bin/pyomo_nsc", "pyomo_old": "/usr/local/bin/pyomo_old", "pyomo_python": "/usr/local/bin/pyomo_python", "pypi_downloads": "/usr/local/bin/pypi_downloads", "pyro_mip_server": "/usr/local/bin/pyro_mip_server", "python3.4": "/usr/local/bin/python3.4", "python3.4-config": "/usr/local/bin/python3.4-config", "python3.4m": "/usr/local/bin/python3.4m", "python3.4m-config": "/usr/local/bin/python3.4m-config", "pyutilib_test_driver": "/usr/local/bin/pyutilib_test_driver", "pyvenv-3.4": "/usr/local/bin/pyvenv-3.4", "readsol": "/usr/local/bin/readsol", "replaceCopyright": "/usr/local/bin/replaceCopyright", "replacecopyright": "/usr/local/bin/replacecopyright", "results_schema": "/usr/local/bin/results_schema", "runbenders": "/usr/local/bin/runbenders", "runef": "/usr/local/bin/runef", "runph": "/usr/local/bin/runph", "test.pyomo": "/usr/local/bin/test.pyomo", "test.pyutilib": "/usr/local/bin/test.pyutilib", "nosetests": "/usr/local/bin/nosetests", "tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config", "pyvenv": "/usr/local/bin/pyvenv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pyomo.
shpc-registry automated BioContainers addition for pyomo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pyomo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pyomo:4.1.10527--py34_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pyomo/4.1.10527--py34_0
$ module help quay.io/biocontainers/pyomo/4.1.10527--py34_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pyomo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pyomo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pyomo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pyomo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pyomo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pyomo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.4

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.4
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### OSSolverService

```bash
$ singularity exec <container> /usr/local/bin/OSSolverService
$ podman run --it --rm --entrypoint /usr/local/bin/OSSolverService   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/OSSolverService   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PyomoOSSolverService

```bash
$ singularity exec <container> /usr/local/bin/PyomoOSSolverService
$ podman run --it --rm --entrypoint /usr/local/bin/PyomoOSSolverService   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PyomoOSSolverService   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checkCopyright

```bash
$ singularity exec <container> /usr/local/bin/checkCopyright
$ podman run --it --rm --entrypoint /usr/local/bin/checkCopyright   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checkCopyright   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checkcopyright

```bash
$ singularity exec <container> /usr/local/bin/checkcopyright
$ podman run --it --rm --entrypoint /usr/local/bin/checkcopyright   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checkcopyright   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### computeconf

```bash
$ singularity exec <container> /usr/local/bin/computeconf
$ podman run --it --rm --entrypoint /usr/local/bin/computeconf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/computeconf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dispatch_srvr

```bash
$ singularity exec <container> /usr/local/bin/dispatch_srvr
$ podman run --it --rm --entrypoint /usr/local/bin/dispatch_srvr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dispatch_srvr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### easy_install-3.4

```bash
$ singularity exec <container> /usr/local/bin/easy_install-3.4
$ podman run --it --rm --entrypoint /usr/local/bin/easy_install-3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easy_install-3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.4

```bash
$ singularity exec <container> /usr/local/bin/idle3.4
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kill_pyro_mip_servers

```bash
$ singularity exec <container> /usr/local/bin/kill_pyro_mip_servers
$ podman run --it --rm --entrypoint /usr/local/bin/kill_pyro_mip_servers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kill_pyro_mip_servers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### launch_pyro_mip_servers

```bash
$ singularity exec <container> /usr/local/bin/launch_pyro_mip_servers
$ podman run --it --rm --entrypoint /usr/local/bin/launch_pyro_mip_servers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/launch_pyro_mip_servers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lbin

```bash
$ singularity exec <container> /usr/local/bin/lbin
$ podman run --it --rm --entrypoint /usr/local/bin/lbin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lbin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lpython

```bash
$ singularity exec <container> /usr/local/bin/lpython
$ podman run --it --rm --entrypoint /usr/local/bin/lpython   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lpython   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phsolverserver

```bash
$ singularity exec <container> /usr/local/bin/phsolverserver
$ podman run --it --rm --entrypoint /usr/local/bin/phsolverserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phsolverserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.4

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.4
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyomo

```bash
$ singularity exec <container> /usr/local/bin/pyomo
$ podman run --it --rm --entrypoint /usr/local/bin/pyomo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyomo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyomo_ns

```bash
$ singularity exec <container> /usr/local/bin/pyomo_ns
$ podman run --it --rm --entrypoint /usr/local/bin/pyomo_ns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyomo_ns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyomo_nsc

```bash
$ singularity exec <container> /usr/local/bin/pyomo_nsc
$ podman run --it --rm --entrypoint /usr/local/bin/pyomo_nsc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyomo_nsc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyomo_old

```bash
$ singularity exec <container> /usr/local/bin/pyomo_old
$ podman run --it --rm --entrypoint /usr/local/bin/pyomo_old   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyomo_old   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyomo_python

```bash
$ singularity exec <container> /usr/local/bin/pyomo_python
$ podman run --it --rm --entrypoint /usr/local/bin/pyomo_python   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyomo_python   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pypi_downloads

```bash
$ singularity exec <container> /usr/local/bin/pypi_downloads
$ podman run --it --rm --entrypoint /usr/local/bin/pypi_downloads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pypi_downloads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyro_mip_server

```bash
$ singularity exec <container> /usr/local/bin/pyro_mip_server
$ podman run --it --rm --entrypoint /usr/local/bin/pyro_mip_server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyro_mip_server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.4

```bash
$ singularity exec <container> /usr/local/bin/python3.4
$ podman run --it --rm --entrypoint /usr/local/bin/python3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.4-config

```bash
$ singularity exec <container> /usr/local/bin/python3.4-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.4-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.4-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.4m

```bash
$ singularity exec <container> /usr/local/bin/python3.4m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.4m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.4m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.4m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.4m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.4m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.4m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyutilib_test_driver

```bash
$ singularity exec <container> /usr/local/bin/pyutilib_test_driver
$ podman run --it --rm --entrypoint /usr/local/bin/pyutilib_test_driver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyutilib_test_driver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.4

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.4
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### readsol

```bash
$ singularity exec <container> /usr/local/bin/readsol
$ podman run --it --rm --entrypoint /usr/local/bin/readsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/readsol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### replaceCopyright

```bash
$ singularity exec <container> /usr/local/bin/replaceCopyright
$ podman run --it --rm --entrypoint /usr/local/bin/replaceCopyright   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/replaceCopyright   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### replacecopyright

```bash
$ singularity exec <container> /usr/local/bin/replacecopyright
$ podman run --it --rm --entrypoint /usr/local/bin/replacecopyright   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/replacecopyright   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### results_schema

```bash
$ singularity exec <container> /usr/local/bin/results_schema
$ podman run --it --rm --entrypoint /usr/local/bin/results_schema   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/results_schema   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runbenders

```bash
$ singularity exec <container> /usr/local/bin/runbenders
$ podman run --it --rm --entrypoint /usr/local/bin/runbenders   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runbenders   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runef

```bash
$ singularity exec <container> /usr/local/bin/runef
$ podman run --it --rm --entrypoint /usr/local/bin/runef   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runef   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runph

```bash
$ singularity exec <container> /usr/local/bin/runph
$ podman run --it --rm --entrypoint /usr/local/bin/runph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test.pyomo

```bash
$ singularity exec <container> /usr/local/bin/test.pyomo
$ podman run --it --rm --entrypoint /usr/local/bin/test.pyomo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test.pyomo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test.pyutilib

```bash
$ singularity exec <container> /usr/local/bin/test.pyutilib
$ podman run --it --rm --entrypoint /usr/local/bin/test.pyutilib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test.pyutilib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nosetests

```bash
$ singularity exec <container> /usr/local/bin/nosetests
$ podman run --it --rm --entrypoint /usr/local/bin/nosetests   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nosetests   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tclsh8.5

```bash
$ singularity exec <container> /usr/local/bin/tclsh8.5
$ podman run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wish8.5

```bash
$ singularity exec <container> /usr/local/bin/wish8.5
$ podman run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncurses5-config

```bash
$ singularity exec <container> /usr/local/bin/ncurses5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncursesw5-config

```bash
$ singularity exec <container> /usr/local/bin/ncursesw5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv

```bash
$ singularity exec <container> /usr/local/bin/pyvenv
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)