---
layout: container
name:  "quay.io/biocontainers/thermorawfileparser"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/thermorawfileparser/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/thermorawfileparser/container.yaml"
updated_at: "2022-11-02 00:19:15.742775"
latest: "1.4.0--ha8f3691_0"
container_url: "https://biocontainers.pro/tools/thermorawfileparser"
aliases:
 - "AWS.Logger.Core.pdb"
 - "AWSSDK.CloudWatchLogs.pdb"
 - "AWSSDK.Core.pdb"
 - "AWSSDK.S3.pdb"
 - "LICENSE"
 - "NUnit3.TestAdapter.pdb"
 - "THERMO_LICENSE"
 - "ThermoRawFileParser"
 - "ThermoRawFileParser.exe"
 - "ThermoRawFileParser.exe.config"
 - "ThermoRawFileParser.pdb"
 - "ThermoRawFileParser.sh"
 - "csc"
 - "csc-dim"
 - "csi"
 - "illinkanalyzer"
 - "monograph"
 - "nunit-console"
 - "nunit-console2"
 - "nunit-console4"
 - "thermorawfileparser"
 - "vbc"
 - "mono-package-runtime"
 - "sgen-grep-binprot"
 - "al"
 - "al2"
 - "caspol"
 - "cccheck"
 - "ccrewrite"
 - "cert-sync"
 - "cert2spc"
 - "certmgr"
versions:
 - "1.4.0--ha8f3691_0"
description: "shpc-registry automated BioContainers addition for thermorawfileparser"
config: {"url": "https://biocontainers.pro/tools/thermorawfileparser", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for thermorawfileparser", "latest": {"1.4.0--ha8f3691_0": "sha256:76c17e3124b723f271bc3d5cf0555650288676bb1a827bd1bae9bb684444a404"}, "tags": {"1.4.0--ha8f3691_0": "sha256:76c17e3124b723f271bc3d5cf0555650288676bb1a827bd1bae9bb684444a404"}, "docker": "quay.io/biocontainers/thermorawfileparser", "aliases": {"AWS.Logger.Core.pdb": "/usr/local/bin/AWS.Logger.Core.pdb", "AWSSDK.CloudWatchLogs.pdb": "/usr/local/bin/AWSSDK.CloudWatchLogs.pdb", "AWSSDK.Core.pdb": "/usr/local/bin/AWSSDK.Core.pdb", "AWSSDK.S3.pdb": "/usr/local/bin/AWSSDK.S3.pdb", "LICENSE": "/usr/local/bin/LICENSE", "NUnit3.TestAdapter.pdb": "/usr/local/bin/NUnit3.TestAdapter.pdb", "THERMO_LICENSE": "/usr/local/bin/THERMO_LICENSE", "ThermoRawFileParser": "/usr/local/bin/ThermoRawFileParser", "ThermoRawFileParser.exe": "/usr/local/bin/ThermoRawFileParser.exe", "ThermoRawFileParser.exe.config": "/usr/local/bin/ThermoRawFileParser.exe.config", "ThermoRawFileParser.pdb": "/usr/local/bin/ThermoRawFileParser.pdb", "ThermoRawFileParser.sh": "/usr/local/bin/ThermoRawFileParser.sh", "csc": "/usr/local/bin/csc", "csc-dim": "/usr/local/bin/csc-dim", "csi": "/usr/local/bin/csi", "illinkanalyzer": "/usr/local/bin/illinkanalyzer", "monograph": "/usr/local/bin/monograph", "nunit-console": "/usr/local/bin/nunit-console", "nunit-console2": "/usr/local/bin/nunit-console2", "nunit-console4": "/usr/local/bin/nunit-console4", "thermorawfileparser": "/usr/local/bin/thermorawfileparser", "vbc": "/usr/local/bin/vbc", "mono-package-runtime": "/usr/local/bin/mono-package-runtime", "sgen-grep-binprot": "/usr/local/bin/sgen-grep-binprot", "al": "/usr/local/bin/al", "al2": "/usr/local/bin/al2", "caspol": "/usr/local/bin/caspol", "cccheck": "/usr/local/bin/cccheck", "ccrewrite": "/usr/local/bin/ccrewrite", "cert-sync": "/usr/local/bin/cert-sync", "cert2spc": "/usr/local/bin/cert2spc", "certmgr": "/usr/local/bin/certmgr"}}
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


#### LICENSE

```bash
$ singularity exec <container> /usr/local/bin/LICENSE
$ podman run --it --rm --entrypoint /usr/local/bin/LICENSE   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LICENSE   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### ThermoRawFileParser.exe.config

```bash
$ singularity exec <container> /usr/local/bin/ThermoRawFileParser.exe.config
$ podman run --it --rm --entrypoint /usr/local/bin/ThermoRawFileParser.exe.config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ThermoRawFileParser.exe.config   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### csc

```bash
$ singularity exec <container> /usr/local/bin/csc
$ podman run --it --rm --entrypoint /usr/local/bin/csc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csc-dim

```bash
$ singularity exec <container> /usr/local/bin/csc-dim
$ podman run --it --rm --entrypoint /usr/local/bin/csc-dim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csc-dim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csi

```bash
$ singularity exec <container> /usr/local/bin/csi
$ podman run --it --rm --entrypoint /usr/local/bin/csi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### illinkanalyzer

```bash
$ singularity exec <container> /usr/local/bin/illinkanalyzer
$ podman run --it --rm --entrypoint /usr/local/bin/illinkanalyzer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/illinkanalyzer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### monograph

```bash
$ singularity exec <container> /usr/local/bin/monograph
$ podman run --it --rm --entrypoint /usr/local/bin/monograph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/monograph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nunit-console

```bash
$ singularity exec <container> /usr/local/bin/nunit-console
$ podman run --it --rm --entrypoint /usr/local/bin/nunit-console   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nunit-console   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nunit-console2

```bash
$ singularity exec <container> /usr/local/bin/nunit-console2
$ podman run --it --rm --entrypoint /usr/local/bin/nunit-console2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nunit-console2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nunit-console4

```bash
$ singularity exec <container> /usr/local/bin/nunit-console4
$ podman run --it --rm --entrypoint /usr/local/bin/nunit-console4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nunit-console4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### thermorawfileparser

```bash
$ singularity exec <container> /usr/local/bin/thermorawfileparser
$ podman run --it --rm --entrypoint /usr/local/bin/thermorawfileparser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/thermorawfileparser   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vbc

```bash
$ singularity exec <container> /usr/local/bin/vbc
$ podman run --it --rm --entrypoint /usr/local/bin/vbc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vbc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mono-package-runtime

```bash
$ singularity exec <container> /usr/local/bin/mono-package-runtime
$ podman run --it --rm --entrypoint /usr/local/bin/mono-package-runtime   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mono-package-runtime   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sgen-grep-binprot

```bash
$ singularity exec <container> /usr/local/bin/sgen-grep-binprot
$ podman run --it --rm --entrypoint /usr/local/bin/sgen-grep-binprot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sgen-grep-binprot   -v ${PWD} -w ${PWD} <container> -c " $@"
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