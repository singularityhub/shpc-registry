---
layout: container
name:  "quay.io/biocontainers/hlama"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hlama/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/hlama/container.yaml"
updated_at: "2022-10-29 17:47:38.392363"
latest: "3.0.1--py35_0"
container_url: "https://biocontainers.pro/tools/hlama"
aliases:
 - "OSSolverService"
 - "OptiTypePipeline.py"
 - "checkCopyright"
 - "checkcopyright"
 - "computeconf"
 - "dispatch_srvr"
 - "evaluate_xhat"
 - "get_pyomo_extras"
 - "hlama"
 - "kill_pyro_mip_servers"
 - "launch_pyro_mip_servers"
 - "lbin"
 - "lpython"
 - "ossolverservice"
 - "phsolverserver"
 - "pyomo"
 - "pyomo_ns"
 - "pyomo_nsc"
 - "pyomo_old"
 - "pyomo_python"
 - "pypi_downloads"
 - "pyro_mip_server"
 - "pyutilib_test_driver"
 - "razers3"
 - "readsol"
 - "replaceCopyright"
 - "replacecopyright"
 - "results_schema"
 - "runbenders"
 - "runef"
 - "runph"
 - "scenariotreeserver"
 - "test.pyomo"
 - "test.pyutilib"
 - "conv-template"
 - "from-template"
 - "nosetests"
 - "pt2to3"
 - "ptdump"
 - "ptrepack"
 - "pttree"
 - "snakemake"
 - "snakemake-bash-completion"
 - "glpsol"
versions:
 - "3.0.1--py35_0"
description: "shpc-registry automated BioContainers addition for hlama"
config: {"url": "https://biocontainers.pro/tools/hlama", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hlama", "latest": {"3.0.1--py35_0": "sha256:252ba196da8cd798bfde329a0232c63565c6a22957436f9f4ae62296db1b91e3"}, "tags": {"3.0.1--py35_0": "sha256:252ba196da8cd798bfde329a0232c63565c6a22957436f9f4ae62296db1b91e3"}, "docker": "quay.io/biocontainers/hlama", "aliases": {"OSSolverService": "/usr/local/bin/OSSolverService", "OptiTypePipeline.py": "/usr/local/bin/OptiTypePipeline.py", "checkCopyright": "/usr/local/bin/checkCopyright", "checkcopyright": "/usr/local/bin/checkcopyright", "computeconf": "/usr/local/bin/computeconf", "dispatch_srvr": "/usr/local/bin/dispatch_srvr", "evaluate_xhat": "/usr/local/bin/evaluate_xhat", "get_pyomo_extras": "/usr/local/bin/get_pyomo_extras", "hlama": "/usr/local/bin/hlama", "kill_pyro_mip_servers": "/usr/local/bin/kill_pyro_mip_servers", "launch_pyro_mip_servers": "/usr/local/bin/launch_pyro_mip_servers", "lbin": "/usr/local/bin/lbin", "lpython": "/usr/local/bin/lpython", "ossolverservice": "/usr/local/bin/ossolverservice", "phsolverserver": "/usr/local/bin/phsolverserver", "pyomo": "/usr/local/bin/pyomo", "pyomo_ns": "/usr/local/bin/pyomo_ns", "pyomo_nsc": "/usr/local/bin/pyomo_nsc", "pyomo_old": "/usr/local/bin/pyomo_old", "pyomo_python": "/usr/local/bin/pyomo_python", "pypi_downloads": "/usr/local/bin/pypi_downloads", "pyro_mip_server": "/usr/local/bin/pyro_mip_server", "pyutilib_test_driver": "/usr/local/bin/pyutilib_test_driver", "razers3": "/usr/local/bin/razers3", "readsol": "/usr/local/bin/readsol", "replaceCopyright": "/usr/local/bin/replaceCopyright", "replacecopyright": "/usr/local/bin/replacecopyright", "results_schema": "/usr/local/bin/results_schema", "runbenders": "/usr/local/bin/runbenders", "runef": "/usr/local/bin/runef", "runph": "/usr/local/bin/runph", "scenariotreeserver": "/usr/local/bin/scenariotreeserver", "test.pyomo": "/usr/local/bin/test.pyomo", "test.pyutilib": "/usr/local/bin/test.pyutilib", "conv-template": "/usr/local/bin/conv-template", "from-template": "/usr/local/bin/from-template", "nosetests": "/usr/local/bin/nosetests", "pt2to3": "/usr/local/bin/pt2to3", "ptdump": "/usr/local/bin/ptdump", "ptrepack": "/usr/local/bin/ptrepack", "pttree": "/usr/local/bin/pttree", "snakemake": "/usr/local/bin/snakemake", "snakemake-bash-completion": "/usr/local/bin/snakemake-bash-completion", "glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hlama.
shpc-registry automated BioContainers addition for hlama
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hlama
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hlama:3.0.1--py35_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hlama/3.0.1--py35_0
$ module help quay.io/biocontainers/hlama/3.0.1--py35_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hlama-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hlama-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hlama-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hlama-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hlama-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hlama-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### OSSolverService

```bash
$ singularity exec <container> /usr/local/bin/OSSolverService
$ podman run --it --rm --entrypoint /usr/local/bin/OSSolverService   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/OSSolverService   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### OptiTypePipeline.py

```bash
$ singularity exec <container> /usr/local/bin/OptiTypePipeline.py
$ podman run --it --rm --entrypoint /usr/local/bin/OptiTypePipeline.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/OptiTypePipeline.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### evaluate_xhat

```bash
$ singularity exec <container> /usr/local/bin/evaluate_xhat
$ podman run --it --rm --entrypoint /usr/local/bin/evaluate_xhat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/evaluate_xhat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_pyomo_extras

```bash
$ singularity exec <container> /usr/local/bin/get_pyomo_extras
$ podman run --it --rm --entrypoint /usr/local/bin/get_pyomo_extras   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_pyomo_extras   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hlama

```bash
$ singularity exec <container> /usr/local/bin/hlama
$ podman run --it --rm --entrypoint /usr/local/bin/hlama   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hlama   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### ossolverservice

```bash
$ singularity exec <container> /usr/local/bin/ossolverservice
$ podman run --it --rm --entrypoint /usr/local/bin/ossolverservice   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ossolverservice   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phsolverserver

```bash
$ singularity exec <container> /usr/local/bin/phsolverserver
$ podman run --it --rm --entrypoint /usr/local/bin/phsolverserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phsolverserver   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### pyutilib_test_driver

```bash
$ singularity exec <container> /usr/local/bin/pyutilib_test_driver
$ podman run --it --rm --entrypoint /usr/local/bin/pyutilib_test_driver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyutilib_test_driver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### razers3

```bash
$ singularity exec <container> /usr/local/bin/razers3
$ podman run --it --rm --entrypoint /usr/local/bin/razers3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/razers3   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### scenariotreeserver

```bash
$ singularity exec <container> /usr/local/bin/scenariotreeserver
$ podman run --it --rm --entrypoint /usr/local/bin/scenariotreeserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scenariotreeserver   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### conv-template

```bash
$ singularity exec <container> /usr/local/bin/conv-template
$ podman run --it --rm --entrypoint /usr/local/bin/conv-template   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conv-template   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### from-template

```bash
$ singularity exec <container> /usr/local/bin/from-template
$ podman run --it --rm --entrypoint /usr/local/bin/from-template   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/from-template   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nosetests

```bash
$ singularity exec <container> /usr/local/bin/nosetests
$ podman run --it --rm --entrypoint /usr/local/bin/nosetests   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nosetests   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pt2to3

```bash
$ singularity exec <container> /usr/local/bin/pt2to3
$ podman run --it --rm --entrypoint /usr/local/bin/pt2to3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pt2to3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ptdump

```bash
$ singularity exec <container> /usr/local/bin/ptdump
$ podman run --it --rm --entrypoint /usr/local/bin/ptdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ptdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ptrepack

```bash
$ singularity exec <container> /usr/local/bin/ptrepack
$ podman run --it --rm --entrypoint /usr/local/bin/ptrepack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ptrepack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pttree

```bash
$ singularity exec <container> /usr/local/bin/pttree
$ podman run --it --rm --entrypoint /usr/local/bin/pttree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pttree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snakemake

```bash
$ singularity exec <container> /usr/local/bin/snakemake
$ podman run --it --rm --entrypoint /usr/local/bin/snakemake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snakemake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snakemake-bash-completion

```bash
$ singularity exec <container> /usr/local/bin/snakemake-bash-completion
$ podman run --it --rm --entrypoint /usr/local/bin/snakemake-bash-completion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snakemake-bash-completion   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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