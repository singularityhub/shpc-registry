---
layout: container
name:  "quay.io/biocontainers/influx_si"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/influx_si/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/influx_si/container.yaml"
updated_at: "2023-11-01 03:20:43.080089"
latest: "7.0.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/influx_si"
aliases:
 - "ff2ftbl"
 - "ff2ftbl.py"
 - "ftbl2code"
 - "ftbl2code.py"
 - "ftbl2cumoAb"
 - "ftbl2cumoAb.py"
 - "ftbl2kvh"
 - "ftbl2kvh.py"
 - "ftbl2labcin"
 - "ftbl2labcin.py"
 - "ftbl2metxml"
 - "ftbl2metxml.py"
 - "ftbl2mtf"
 - "ftbl2mtf.py"
 - "ftbl2netan"
 - "ftbl2netan.py"
 - "ftbl2optR"
 - "ftbl2optR.py"
 - "ftbl2xgmml"
 - "ftbl2xgmml.py"
 - "influx_i"
 - "influx_i.py"
 - "influx_s"
 - "influx_s.py"
 - "res2ftbl_meas"
 - "res2ftbl_meas.py"
 - "txt2ftbl"
 - "txt2ftbl.py"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
versions:
 - "6.1--pyhdfd78af_0"
 - "7.0--pyhdfd78af_0"
 - "7.0.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for influx_si"
config: {"url": "https://biocontainers.pro/tools/influx_si", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for influx_si", "latest": {"7.0.1--pyhdfd78af_0": "sha256:06e6c91021049552370f490636f20b0b1ab887bfc9d64bce8cc9c69161a2a0d5"}, "tags": {"6.1--pyhdfd78af_0": "sha256:ac0352104547261057cc19c24e0b82ff2385f894563b08cb339ff40ee9bb53e5", "7.0--pyhdfd78af_0": "sha256:4980fbec71a4aa6708fad9a0c58d7d3cb9c523be75a9b085d926d829d285e961", "7.0.1--pyhdfd78af_0": "sha256:06e6c91021049552370f490636f20b0b1ab887bfc9d64bce8cc9c69161a2a0d5"}, "docker": "quay.io/biocontainers/influx_si", "aliases": {"ff2ftbl": "/usr/local/bin/ff2ftbl", "ff2ftbl.py": "/usr/local/bin/ff2ftbl.py", "ftbl2code": "/usr/local/bin/ftbl2code", "ftbl2code.py": "/usr/local/bin/ftbl2code.py", "ftbl2cumoAb": "/usr/local/bin/ftbl2cumoAb", "ftbl2cumoAb.py": "/usr/local/bin/ftbl2cumoAb.py", "ftbl2kvh": "/usr/local/bin/ftbl2kvh", "ftbl2kvh.py": "/usr/local/bin/ftbl2kvh.py", "ftbl2labcin": "/usr/local/bin/ftbl2labcin", "ftbl2labcin.py": "/usr/local/bin/ftbl2labcin.py", "ftbl2metxml": "/usr/local/bin/ftbl2metxml", "ftbl2metxml.py": "/usr/local/bin/ftbl2metxml.py", "ftbl2mtf": "/usr/local/bin/ftbl2mtf", "ftbl2mtf.py": "/usr/local/bin/ftbl2mtf.py", "ftbl2netan": "/usr/local/bin/ftbl2netan", "ftbl2netan.py": "/usr/local/bin/ftbl2netan.py", "ftbl2optR": "/usr/local/bin/ftbl2optR", "ftbl2optR.py": "/usr/local/bin/ftbl2optR.py", "ftbl2xgmml": "/usr/local/bin/ftbl2xgmml", "ftbl2xgmml.py": "/usr/local/bin/ftbl2xgmml.py", "influx_i": "/usr/local/bin/influx_i", "influx_i.py": "/usr/local/bin/influx_i.py", "influx_s": "/usr/local/bin/influx_s", "influx_s.py": "/usr/local/bin/influx_s.py", "res2ftbl_meas": "/usr/local/bin/res2ftbl_meas", "res2ftbl_meas.py": "/usr/local/bin/res2ftbl_meas.py", "txt2ftbl": "/usr/local/bin/txt2ftbl", "txt2ftbl.py": "/usr/local/bin/txt2ftbl.py", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/influx_si.
shpc-registry automated BioContainers addition for influx_si
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/influx_si
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/influx_si:7.0.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/influx_si/7.0.1--pyhdfd78af_0
$ module help quay.io/biocontainers/influx_si/7.0.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### influx_si-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### influx_si-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### influx_si-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### influx_si-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### influx_si-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### influx_si-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ff2ftbl

```bash
$ singularity exec <container> /usr/local/bin/ff2ftbl
$ podman run --it --rm --entrypoint /usr/local/bin/ff2ftbl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ff2ftbl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ff2ftbl.py

```bash
$ singularity exec <container> /usr/local/bin/ff2ftbl.py
$ podman run --it --rm --entrypoint /usr/local/bin/ff2ftbl.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ff2ftbl.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ftbl2code

```bash
$ singularity exec <container> /usr/local/bin/ftbl2code
$ podman run --it --rm --entrypoint /usr/local/bin/ftbl2code   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ftbl2code   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ftbl2code.py

```bash
$ singularity exec <container> /usr/local/bin/ftbl2code.py
$ podman run --it --rm --entrypoint /usr/local/bin/ftbl2code.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ftbl2code.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ftbl2cumoAb

```bash
$ singularity exec <container> /usr/local/bin/ftbl2cumoAb
$ podman run --it --rm --entrypoint /usr/local/bin/ftbl2cumoAb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ftbl2cumoAb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ftbl2cumoAb.py

```bash
$ singularity exec <container> /usr/local/bin/ftbl2cumoAb.py
$ podman run --it --rm --entrypoint /usr/local/bin/ftbl2cumoAb.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ftbl2cumoAb.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ftbl2kvh

```bash
$ singularity exec <container> /usr/local/bin/ftbl2kvh
$ podman run --it --rm --entrypoint /usr/local/bin/ftbl2kvh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ftbl2kvh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ftbl2kvh.py

```bash
$ singularity exec <container> /usr/local/bin/ftbl2kvh.py
$ podman run --it --rm --entrypoint /usr/local/bin/ftbl2kvh.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ftbl2kvh.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ftbl2labcin

```bash
$ singularity exec <container> /usr/local/bin/ftbl2labcin
$ podman run --it --rm --entrypoint /usr/local/bin/ftbl2labcin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ftbl2labcin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ftbl2labcin.py

```bash
$ singularity exec <container> /usr/local/bin/ftbl2labcin.py
$ podman run --it --rm --entrypoint /usr/local/bin/ftbl2labcin.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ftbl2labcin.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ftbl2metxml

```bash
$ singularity exec <container> /usr/local/bin/ftbl2metxml
$ podman run --it --rm --entrypoint /usr/local/bin/ftbl2metxml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ftbl2metxml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ftbl2metxml.py

```bash
$ singularity exec <container> /usr/local/bin/ftbl2metxml.py
$ podman run --it --rm --entrypoint /usr/local/bin/ftbl2metxml.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ftbl2metxml.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ftbl2mtf

```bash
$ singularity exec <container> /usr/local/bin/ftbl2mtf
$ podman run --it --rm --entrypoint /usr/local/bin/ftbl2mtf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ftbl2mtf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ftbl2mtf.py

```bash
$ singularity exec <container> /usr/local/bin/ftbl2mtf.py
$ podman run --it --rm --entrypoint /usr/local/bin/ftbl2mtf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ftbl2mtf.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ftbl2netan

```bash
$ singularity exec <container> /usr/local/bin/ftbl2netan
$ podman run --it --rm --entrypoint /usr/local/bin/ftbl2netan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ftbl2netan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ftbl2netan.py

```bash
$ singularity exec <container> /usr/local/bin/ftbl2netan.py
$ podman run --it --rm --entrypoint /usr/local/bin/ftbl2netan.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ftbl2netan.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ftbl2optR

```bash
$ singularity exec <container> /usr/local/bin/ftbl2optR
$ podman run --it --rm --entrypoint /usr/local/bin/ftbl2optR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ftbl2optR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ftbl2optR.py

```bash
$ singularity exec <container> /usr/local/bin/ftbl2optR.py
$ podman run --it --rm --entrypoint /usr/local/bin/ftbl2optR.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ftbl2optR.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ftbl2xgmml

```bash
$ singularity exec <container> /usr/local/bin/ftbl2xgmml
$ podman run --it --rm --entrypoint /usr/local/bin/ftbl2xgmml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ftbl2xgmml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ftbl2xgmml.py

```bash
$ singularity exec <container> /usr/local/bin/ftbl2xgmml.py
$ podman run --it --rm --entrypoint /usr/local/bin/ftbl2xgmml.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ftbl2xgmml.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### influx_i

```bash
$ singularity exec <container> /usr/local/bin/influx_i
$ podman run --it --rm --entrypoint /usr/local/bin/influx_i   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/influx_i   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### influx_i.py

```bash
$ singularity exec <container> /usr/local/bin/influx_i.py
$ podman run --it --rm --entrypoint /usr/local/bin/influx_i.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/influx_i.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### influx_s

```bash
$ singularity exec <container> /usr/local/bin/influx_s
$ podman run --it --rm --entrypoint /usr/local/bin/influx_s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/influx_s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### influx_s.py

```bash
$ singularity exec <container> /usr/local/bin/influx_s.py
$ podman run --it --rm --entrypoint /usr/local/bin/influx_s.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/influx_s.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### res2ftbl_meas

```bash
$ singularity exec <container> /usr/local/bin/res2ftbl_meas
$ podman run --it --rm --entrypoint /usr/local/bin/res2ftbl_meas   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/res2ftbl_meas   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### res2ftbl_meas.py

```bash
$ singularity exec <container> /usr/local/bin/res2ftbl_meas.py
$ podman run --it --rm --entrypoint /usr/local/bin/res2ftbl_meas.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/res2ftbl_meas.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### txt2ftbl

```bash
$ singularity exec <container> /usr/local/bin/txt2ftbl
$ podman run --it --rm --entrypoint /usr/local/bin/txt2ftbl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/txt2ftbl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### txt2ftbl.py

```bash
$ singularity exec <container> /usr/local/bin/txt2ftbl.py
$ podman run --it --rm --entrypoint /usr/local/bin/txt2ftbl.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/txt2ftbl.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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