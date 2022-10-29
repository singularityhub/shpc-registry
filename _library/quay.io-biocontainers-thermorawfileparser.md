---
layout: container
name:  "quay.io/biocontainers/thermorawfileparser"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/thermorawfileparser/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/thermorawfileparser/container.yaml"
updated_at: "2022-10-29 05:34:12.446410"
latest: "1.4.0--ha8f3691_0"
container_url: "https://biocontainers.pro/tools/thermorawfileparser"
aliases:
 - "AWS.Logger.Core.pdb"
 - "AWSSDK.CloudWatchLogs.pdb"
 - "AWSSDK.Core.pdb"
 - "AWSSDK.S3.pdb"
 - "NUnit3.TestAdapter.pdb"
 - "THERMO_LICENSE"
 - "ThermoRawFileParser"
 - "ThermoRawFileParser.exe"
 - "ThermoRawFileParser.pdb"
 - "ThermoRawFileParser.sh"
 - "thermorawfileparser"
 - "LICENSE"
 - "al"
 - "al2"
 - "build_env_setup.sh"
 - "caspol"
 - "cccheck"
 - "ccrewrite"
 - "cert-sync"
 - "cert2spc"
 - "certmgr"
versions:
 - "1.4.0--ha8f3691_0"
description: "shpc-registry automated BioContainers addition for thermorawfileparser"
config: {"url": "https://biocontainers.pro/tools/thermorawfileparser", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for thermorawfileparser", "latest": {"1.4.0--ha8f3691_0": "sha256:76c17e3124b723f271bc3d5cf0555650288676bb1a827bd1bae9bb684444a404"}, "tags": {"1.4.0--ha8f3691_0": "sha256:76c17e3124b723f271bc3d5cf0555650288676bb1a827bd1bae9bb684444a404"}, "docker": "quay.io/biocontainers/thermorawfileparser", "aliases": {"AWS.Logger.Core.pdb": "/usr/local/bin/AWS.Logger.Core.pdb", "AWSSDK.CloudWatchLogs.pdb": "/usr/local/bin/AWSSDK.CloudWatchLogs.pdb", "AWSSDK.Core.pdb": "/usr/local/bin/AWSSDK.Core.pdb", "AWSSDK.S3.pdb": "/usr/local/bin/AWSSDK.S3.pdb", "NUnit3.TestAdapter.pdb": "/usr/local/bin/NUnit3.TestAdapter.pdb", "THERMO_LICENSE": "/usr/local/bin/THERMO_LICENSE", "ThermoRawFileParser": "/usr/local/bin/ThermoRawFileParser", "ThermoRawFileParser.exe": "/usr/local/bin/ThermoRawFileParser.exe", "ThermoRawFileParser.pdb": "/usr/local/bin/ThermoRawFileParser.pdb", "ThermoRawFileParser.sh": "/usr/local/bin/ThermoRawFileParser.sh", "thermorawfileparser": "/usr/local/bin/thermorawfileparser", "LICENSE": "/usr/local/bin/LICENSE", "al": "/usr/local/bin/al", "al2": "/usr/local/bin/al2", "build_env_setup.sh": "/usr/local/bin/build_env_setup.sh", "caspol": "/usr/local/bin/caspol", "cccheck": "/usr/local/bin/cccheck", "ccrewrite": "/usr/local/bin/ccrewrite", "cert-sync": "/usr/local/bin/cert-sync", "cert2spc": "/usr/local/bin/cert2spc", "certmgr": "/usr/local/bin/certmgr"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/thermorawfileparser.
shpc-registry automated BioContainers addition for thermorawfileparser
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/thermorawfileparser
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/thermorawfileparser:1.4.0--ha8f3691_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/thermorawfileparser/1.4.0--ha8f3691_0
$ module help quay.io/biocontainers/thermorawfileparser/1.4.0--ha8f3691_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### thermorawfileparser-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### thermorawfileparser-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### thermorawfileparser-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### thermorawfileparser-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### thermorawfileparser-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### thermorawfileparser-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### AWS.Logger.Core.pdb

```bash
$ singularity exec <container> /usr/local/bin/AWS.Logger.Core.pdb
$ podman run --it --rm --entrypoint /usr/local/bin/AWS.Logger.Core.pdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AWS.Logger.Core.pdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AWSSDK.CloudWatchLogs.pdb

```bash
$ singularity exec <container> /usr/local/bin/AWSSDK.CloudWatchLogs.pdb
$ podman run --it --rm --entrypoint /usr/local/bin/AWSSDK.CloudWatchLogs.pdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AWSSDK.CloudWatchLogs.pdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AWSSDK.Core.pdb

```bash
$ singularity exec <container> /usr/local/bin/AWSSDK.Core.pdb
$ podman run --it --rm --entrypoint /usr/local/bin/AWSSDK.Core.pdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AWSSDK.Core.pdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AWSSDK.S3.pdb

```bash
$ singularity exec <container> /usr/local/bin/AWSSDK.S3.pdb
$ podman run --it --rm --entrypoint /usr/local/bin/AWSSDK.S3.pdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AWSSDK.S3.pdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### NUnit3.TestAdapter.pdb

```bash
$ singularity exec <container> /usr/local/bin/NUnit3.TestAdapter.pdb
$ podman run --it --rm --entrypoint /usr/local/bin/NUnit3.TestAdapter.pdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/NUnit3.TestAdapter.pdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### THERMO_LICENSE

```bash
$ singularity exec <container> /usr/local/bin/THERMO_LICENSE
$ podman run --it --rm --entrypoint /usr/local/bin/THERMO_LICENSE   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/THERMO_LICENSE   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ThermoRawFileParser

```bash
$ singularity exec <container> /usr/local/bin/ThermoRawFileParser
$ podman run --it --rm --entrypoint /usr/local/bin/ThermoRawFileParser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ThermoRawFileParser   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ThermoRawFileParser.exe

```bash
$ singularity exec <container> /usr/local/bin/ThermoRawFileParser.exe
$ podman run --it --rm --entrypoint /usr/local/bin/ThermoRawFileParser.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ThermoRawFileParser.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ThermoRawFileParser.pdb

```bash
$ singularity exec <container> /usr/local/bin/ThermoRawFileParser.pdb
$ podman run --it --rm --entrypoint /usr/local/bin/ThermoRawFileParser.pdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ThermoRawFileParser.pdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ThermoRawFileParser.sh

```bash
$ singularity exec <container> /usr/local/bin/ThermoRawFileParser.sh
$ podman run --it --rm --entrypoint /usr/local/bin/ThermoRawFileParser.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ThermoRawFileParser.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### thermorawfileparser

```bash
$ singularity exec <container> /usr/local/bin/thermorawfileparser
$ podman run --it --rm --entrypoint /usr/local/bin/thermorawfileparser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/thermorawfileparser   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LICENSE

```bash
$ singularity exec <container> /usr/local/bin/LICENSE
$ podman run --it --rm --entrypoint /usr/local/bin/LICENSE   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LICENSE   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### al

```bash
$ singularity exec <container> /usr/local/bin/al
$ podman run --it --rm --entrypoint /usr/local/bin/al   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/al   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### al2

```bash
$ singularity exec <container> /usr/local/bin/al2
$ podman run --it --rm --entrypoint /usr/local/bin/al2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/al2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### build_env_setup.sh

```bash
$ singularity exec <container> /usr/local/bin/build_env_setup.sh
$ podman run --it --rm --entrypoint /usr/local/bin/build_env_setup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build_env_setup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### caspol

```bash
$ singularity exec <container> /usr/local/bin/caspol
$ podman run --it --rm --entrypoint /usr/local/bin/caspol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/caspol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cccheck

```bash
$ singularity exec <container> /usr/local/bin/cccheck
$ podman run --it --rm --entrypoint /usr/local/bin/cccheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cccheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ccrewrite

```bash
$ singularity exec <container> /usr/local/bin/ccrewrite
$ podman run --it --rm --entrypoint /usr/local/bin/ccrewrite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccrewrite   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cert-sync

```bash
$ singularity exec <container> /usr/local/bin/cert-sync
$ podman run --it --rm --entrypoint /usr/local/bin/cert-sync   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cert-sync   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cert2spc

```bash
$ singularity exec <container> /usr/local/bin/cert2spc
$ podman run --it --rm --entrypoint /usr/local/bin/cert2spc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cert2spc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### certmgr

```bash
$ singularity exec <container> /usr/local/bin/certmgr
$ podman run --it --rm --entrypoint /usr/local/bin/certmgr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/certmgr   -v ${PWD} -w ${PWD} <container> -c " $@"
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