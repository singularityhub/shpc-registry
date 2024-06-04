---
layout: container
name:  "quay.io/biocontainers/maxquant"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/maxquant/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/maxquant/container.yaml"
updated_at: "2024-06-04 03:14:02.729732"
latest: "2.0.3.0--py310hdfd78af_1"
container_url: "https://biocontainers.pro/tools/maxquant"
aliases:
 - "CheckDll.exe"
 - "Contents.xsd"
 - "DefaultMassCal.xsd"
 - "Devices.xsd"
 - "MSActualDefs.xsd"
 - "MSScan_XSpecific.xsd"
 - "MSTS.xsd"
 - "MSTS_XSpecific.xsd"
 - "MaxQuantCmd.exe"
 - "MaxQuantCmd.runtimeconfig.json"
 - "MaxQuantGui.exe"
 - "MaxQuantGui.exe.config"
 - "MaxQuantServer.exe"
 - "MaxQuantTask.exe"
 - "MaxQuantTaskCore.runtimeconfig.json"
 - "MqparConverter.exe"
 - "Sciex.Data.Processing.DLL"
 - "csc"
 - "csc-dim"
 - "csi"
 - "global.json"
 - "illinkanalyzer"
 - "maxquant"
 - "monograph"
 - "nunit-console"
 - "nunit-console2"
 - "nunit-console4"
 - "vbc"
 - "xgboost.lib"
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
 - "2.0.3.0--py310hdfd78af_1"
description: "shpc-registry automated BioContainers addition for maxquant"
config: {"url": "https://biocontainers.pro/tools/maxquant", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for maxquant", "latest": {"2.0.3.0--py310hdfd78af_1": "sha256:3fddb6ffc8888e58537d07991d923f80252015463879b8719d98324ec317f7fe"}, "tags": {"2.0.3.0--py310hdfd78af_1": "sha256:3fddb6ffc8888e58537d07991d923f80252015463879b8719d98324ec317f7fe"}, "docker": "quay.io/biocontainers/maxquant", "aliases": {"CheckDll.exe": "/usr/local/bin/CheckDll.exe", "Contents.xsd": "/usr/local/bin/Contents.xsd", "DefaultMassCal.xsd": "/usr/local/bin/DefaultMassCal.xsd", "Devices.xsd": "/usr/local/bin/Devices.xsd", "MSActualDefs.xsd": "/usr/local/bin/MSActualDefs.xsd", "MSScan_XSpecific.xsd": "/usr/local/bin/MSScan_XSpecific.xsd", "MSTS.xsd": "/usr/local/bin/MSTS.xsd", "MSTS_XSpecific.xsd": "/usr/local/bin/MSTS_XSpecific.xsd", "MaxQuantCmd.exe": "/usr/local/bin/MaxQuantCmd.exe", "MaxQuantCmd.runtimeconfig.json": "/usr/local/bin/MaxQuantCmd.runtimeconfig.json", "MaxQuantGui.exe": "/usr/local/bin/MaxQuantGui.exe", "MaxQuantGui.exe.config": "/usr/local/bin/MaxQuantGui.exe.config", "MaxQuantServer.exe": "/usr/local/bin/MaxQuantServer.exe", "MaxQuantTask.exe": "/usr/local/bin/MaxQuantTask.exe", "MaxQuantTaskCore.runtimeconfig.json": "/usr/local/bin/MaxQuantTaskCore.runtimeconfig.json", "MqparConverter.exe": "/usr/local/bin/MqparConverter.exe", "Sciex.Data.Processing.DLL": "/usr/local/bin/Sciex.Data.Processing.DLL", "csc": "/usr/local/bin/csc", "csc-dim": "/usr/local/bin/csc-dim", "csi": "/usr/local/bin/csi", "global.json": "/usr/local/bin/global.json", "illinkanalyzer": "/usr/local/bin/illinkanalyzer", "maxquant": "/usr/local/bin/maxquant", "monograph": "/usr/local/bin/monograph", "nunit-console": "/usr/local/bin/nunit-console", "nunit-console2": "/usr/local/bin/nunit-console2", "nunit-console4": "/usr/local/bin/nunit-console4", "vbc": "/usr/local/bin/vbc", "xgboost.lib": "/usr/local/bin/xgboost.lib", "mono-package-runtime": "/usr/local/bin/mono-package-runtime", "sgen-grep-binprot": "/usr/local/bin/sgen-grep-binprot", "al": "/usr/local/bin/al", "al2": "/usr/local/bin/al2", "caspol": "/usr/local/bin/caspol", "cccheck": "/usr/local/bin/cccheck", "ccrewrite": "/usr/local/bin/ccrewrite", "cert-sync": "/usr/local/bin/cert-sync", "cert2spc": "/usr/local/bin/cert2spc", "certmgr": "/usr/local/bin/certmgr"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/maxquant.
shpc-registry automated BioContainers addition for maxquant
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/maxquant
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/maxquant:2.0.3.0--py310hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/maxquant/2.0.3.0--py310hdfd78af_1
$ module help quay.io/biocontainers/maxquant/2.0.3.0--py310hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### maxquant-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### maxquant-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### maxquant-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### maxquant-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### maxquant-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### maxquant-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### CheckDll.exe

```bash
$ singularity exec <container> /usr/local/bin/CheckDll.exe
$ podman run --it --rm --entrypoint /usr/local/bin/CheckDll.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CheckDll.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Contents.xsd

```bash
$ singularity exec <container> /usr/local/bin/Contents.xsd
$ podman run --it --rm --entrypoint /usr/local/bin/Contents.xsd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Contents.xsd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DefaultMassCal.xsd

```bash
$ singularity exec <container> /usr/local/bin/DefaultMassCal.xsd
$ podman run --it --rm --entrypoint /usr/local/bin/DefaultMassCal.xsd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DefaultMassCal.xsd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Devices.xsd

```bash
$ singularity exec <container> /usr/local/bin/Devices.xsd
$ podman run --it --rm --entrypoint /usr/local/bin/Devices.xsd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Devices.xsd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MSActualDefs.xsd

```bash
$ singularity exec <container> /usr/local/bin/MSActualDefs.xsd
$ podman run --it --rm --entrypoint /usr/local/bin/MSActualDefs.xsd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MSActualDefs.xsd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MSScan_XSpecific.xsd

```bash
$ singularity exec <container> /usr/local/bin/MSScan_XSpecific.xsd
$ podman run --it --rm --entrypoint /usr/local/bin/MSScan_XSpecific.xsd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MSScan_XSpecific.xsd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MSTS.xsd

```bash
$ singularity exec <container> /usr/local/bin/MSTS.xsd
$ podman run --it --rm --entrypoint /usr/local/bin/MSTS.xsd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MSTS.xsd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MSTS_XSpecific.xsd

```bash
$ singularity exec <container> /usr/local/bin/MSTS_XSpecific.xsd
$ podman run --it --rm --entrypoint /usr/local/bin/MSTS_XSpecific.xsd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MSTS_XSpecific.xsd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MaxQuantCmd.exe

```bash
$ singularity exec <container> /usr/local/bin/MaxQuantCmd.exe
$ podman run --it --rm --entrypoint /usr/local/bin/MaxQuantCmd.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MaxQuantCmd.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MaxQuantCmd.runtimeconfig.json

```bash
$ singularity exec <container> /usr/local/bin/MaxQuantCmd.runtimeconfig.json
$ podman run --it --rm --entrypoint /usr/local/bin/MaxQuantCmd.runtimeconfig.json   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MaxQuantCmd.runtimeconfig.json   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MaxQuantGui.exe

```bash
$ singularity exec <container> /usr/local/bin/MaxQuantGui.exe
$ podman run --it --rm --entrypoint /usr/local/bin/MaxQuantGui.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MaxQuantGui.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MaxQuantGui.exe.config

```bash
$ singularity exec <container> /usr/local/bin/MaxQuantGui.exe.config
$ podman run --it --rm --entrypoint /usr/local/bin/MaxQuantGui.exe.config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MaxQuantGui.exe.config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MaxQuantServer.exe

```bash
$ singularity exec <container> /usr/local/bin/MaxQuantServer.exe
$ podman run --it --rm --entrypoint /usr/local/bin/MaxQuantServer.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MaxQuantServer.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MaxQuantTask.exe

```bash
$ singularity exec <container> /usr/local/bin/MaxQuantTask.exe
$ podman run --it --rm --entrypoint /usr/local/bin/MaxQuantTask.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MaxQuantTask.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MaxQuantTaskCore.runtimeconfig.json

```bash
$ singularity exec <container> /usr/local/bin/MaxQuantTaskCore.runtimeconfig.json
$ podman run --it --rm --entrypoint /usr/local/bin/MaxQuantTaskCore.runtimeconfig.json   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MaxQuantTaskCore.runtimeconfig.json   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MqparConverter.exe

```bash
$ singularity exec <container> /usr/local/bin/MqparConverter.exe
$ podman run --it --rm --entrypoint /usr/local/bin/MqparConverter.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MqparConverter.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Sciex.Data.Processing.DLL

```bash
$ singularity exec <container> /usr/local/bin/Sciex.Data.Processing.DLL
$ podman run --it --rm --entrypoint /usr/local/bin/Sciex.Data.Processing.DLL   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Sciex.Data.Processing.DLL   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### global.json

```bash
$ singularity exec <container> /usr/local/bin/global.json
$ podman run --it --rm --entrypoint /usr/local/bin/global.json   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/global.json   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### illinkanalyzer

```bash
$ singularity exec <container> /usr/local/bin/illinkanalyzer
$ podman run --it --rm --entrypoint /usr/local/bin/illinkanalyzer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/illinkanalyzer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maxquant

```bash
$ singularity exec <container> /usr/local/bin/maxquant
$ podman run --it --rm --entrypoint /usr/local/bin/maxquant   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maxquant   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### vbc

```bash
$ singularity exec <container> /usr/local/bin/vbc
$ podman run --it --rm --entrypoint /usr/local/bin/vbc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vbc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xgboost.lib

```bash
$ singularity exec <container> /usr/local/bin/xgboost.lib
$ podman run --it --rm --entrypoint /usr/local/bin/xgboost.lib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xgboost.lib   -v ${PWD} -w ${PWD} <container> -c " $@"
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