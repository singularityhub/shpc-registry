---
layout: container
name:  "quay.io/biocontainers/optitype"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/optitype/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/optitype/container.yaml"
updated_at: "2024-10-27 03:12:11.798719"
latest: "1.3.5--hdfd78af_2"
container_url: "https://biocontainers.pro/tools/optitype"
aliases:
 - "OSSolverService"
 - "OptiTypePipeline.py"
 - "checkCopyright"
 - "checkcopyright"
 - "computeconf"
 - "config.ini"
 - "dispatch_srvr"
 - "evaluate_xhat"
 - "hlatyper.py"
 - "kill_pyro_mip_servers"
 - "launch_pyro_mip_servers"
 - "lbin"
 - "lpython"
 - "model.py"
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
 - "nosetests-3.9"
 - "nosetests"
 - "pt2to3"
 - "ptdump"
 - "ptrepack"
 - "pttree"
 - "glpsol"
 - "futurize"
 - "pasteurize"
 - "fasta-sanitize.pl"
versions:
 - "1.3.5--hdfd78af_1"
 - "1.3.5--hdfd78af_2"
description: "shpc-registry automated BioContainers addition for optitype"
config: {"url": "https://biocontainers.pro/tools/optitype", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for optitype", "latest": {"1.3.5--hdfd78af_2": "sha256:ed4389ce509f14c7b12c46184fd5a193e5472898d357b172b2dc326c3ab33e39"}, "tags": {"1.3.5--hdfd78af_1": "sha256:92d9b78538911d2faba7f2ae85bdc68cc80806758fd13e468b56764e0a63beb4", "1.3.5--hdfd78af_2": "sha256:ed4389ce509f14c7b12c46184fd5a193e5472898d357b172b2dc326c3ab33e39"}, "docker": "quay.io/biocontainers/optitype", "aliases": {"OSSolverService": "/usr/local/bin/OSSolverService", "OptiTypePipeline.py": "/usr/local/bin/OptiTypePipeline.py", "checkCopyright": "/usr/local/bin/checkCopyright", "checkcopyright": "/usr/local/bin/checkcopyright", "computeconf": "/usr/local/bin/computeconf", "config.ini": "/usr/local/bin/config.ini", "dispatch_srvr": "/usr/local/bin/dispatch_srvr", "evaluate_xhat": "/usr/local/bin/evaluate_xhat", "hlatyper.py": "/usr/local/bin/hlatyper.py", "kill_pyro_mip_servers": "/usr/local/bin/kill_pyro_mip_servers", "launch_pyro_mip_servers": "/usr/local/bin/launch_pyro_mip_servers", "lbin": "/usr/local/bin/lbin", "lpython": "/usr/local/bin/lpython", "model.py": "/usr/local/bin/model.py", "ossolverservice": "/usr/local/bin/ossolverservice", "phsolverserver": "/usr/local/bin/phsolverserver", "pyomo": "/usr/local/bin/pyomo", "pyomo_ns": "/usr/local/bin/pyomo_ns", "pyomo_nsc": "/usr/local/bin/pyomo_nsc", "pyomo_old": "/usr/local/bin/pyomo_old", "pyomo_python": "/usr/local/bin/pyomo_python", "pypi_downloads": "/usr/local/bin/pypi_downloads", "pyro_mip_server": "/usr/local/bin/pyro_mip_server", "pyutilib_test_driver": "/usr/local/bin/pyutilib_test_driver", "razers3": "/usr/local/bin/razers3", "readsol": "/usr/local/bin/readsol", "replaceCopyright": "/usr/local/bin/replaceCopyright", "replacecopyright": "/usr/local/bin/replacecopyright", "results_schema": "/usr/local/bin/results_schema", "runbenders": "/usr/local/bin/runbenders", "runef": "/usr/local/bin/runef", "runph": "/usr/local/bin/runph", "scenariotreeserver": "/usr/local/bin/scenariotreeserver", "test.pyomo": "/usr/local/bin/test.pyomo", "test.pyutilib": "/usr/local/bin/test.pyutilib", "nosetests-3.9": "/usr/local/bin/nosetests-3.9", "nosetests": "/usr/local/bin/nosetests", "pt2to3": "/usr/local/bin/pt2to3", "ptdump": "/usr/local/bin/ptdump", "ptrepack": "/usr/local/bin/ptrepack", "pttree": "/usr/local/bin/pttree", "glpsol": "/usr/local/bin/glpsol", "futurize": "/usr/local/bin/futurize", "pasteurize": "/usr/local/bin/pasteurize", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/optitype.
shpc-registry automated BioContainers addition for optitype
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/optitype
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/optitype:1.3.5--hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/optitype/1.3.5--hdfd78af_2
$ module help quay.io/biocontainers/optitype/1.3.5--hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### optitype-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### optitype-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### optitype-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### optitype-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### optitype-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### optitype-inspect-deffile:

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


#### config.ini

```bash
$ singularity exec <container> /usr/local/bin/config.ini
$ podman run --it --rm --entrypoint /usr/local/bin/config.ini   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/config.ini   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### hlatyper.py

```bash
$ singularity exec <container> /usr/local/bin/hlatyper.py
$ podman run --it --rm --entrypoint /usr/local/bin/hlatyper.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hlatyper.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### model.py

```bash
$ singularity exec <container> /usr/local/bin/model.py
$ podman run --it --rm --entrypoint /usr/local/bin/model.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/model.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### nosetests-3.9

```bash
$ singularity exec <container> /usr/local/bin/nosetests-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/nosetests-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nosetests-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### futurize

```bash
$ singularity exec <container> /usr/local/bin/futurize
$ podman run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pasteurize

```bash
$ singularity exec <container> /usr/local/bin/pasteurize
$ podman run --it --rm --entrypoint /usr/local/bin/pasteurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pasteurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-sanitize.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta-sanitize.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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