---
layout: container
name:  "ghcr.io/autamus/geant4"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/geant4/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/geant4/container.yaml"
updated_at: "2024-02-25 02:23:43.160688"
latest: "11.0.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/geant4"
aliases:
 - "Cast-config"
 - "CreateDOMDocument"
 - "DOMCount"
 - "DOMPrint"
 - "EnumVal"
 - "Evaluator-config"
 - "Exceptions-config"
 - "GenericFunctions-config"
 - "Geometry-config"
 - "Matrix-config"
 - "MemParse"
 - "PParse"
 - "PSVIWriter"
 - "Random-config"
 - "RandomObjects-config"
 - "Redirect"
 - "RefCount-config"
 - "SAX2Count"
 - "SAX2Print"
 - "SAXCount"
 - "SAXPrint"
 - "SCMPrint"
 - "SEnumVal"
 - "StdInParse"
 - "Units-config"
 - "Utility-config"
 - "Vector-config"
 - "XInclude"
 - "geant4-config"
 - "geant4.csh"
 - "geant4.sh"
versions:
 - "10.7.1"
 - "10.7.2"
 - "11.0.0"
 - "latest"
 - "11.0.3"
description: "Geant4 is a platform for the simulation of the passage of particles through matter using Monte Carlo methods."
config: {"docker": "ghcr.io/autamus/geant4", "url": "https://github.com/orgs/autamus/packages/container/package/geant4", "maintainer": "@vsoch", "description": "Geant4 is a platform for the simulation of the passage of particles through matter using Monte Carlo methods.", "latest": {"11.0.0": "sha256:5181b262eaef780d0e571730e41c6162ea7d71e2696d1147f24b16d68b7c7ca5"}, "tags": {"10.7.1": "sha256:50ef5b260eae59c38f2360984095ee1752a0ad212d0f82bcaf6c712c8dda4e02", "10.7.2": "sha256:6c93f83aa3e4c5933d175b1a7777a5907d35033234a2dae47ab0383bc00a98df", "11.0.0": "sha256:5181b262eaef780d0e571730e41c6162ea7d71e2696d1147f24b16d68b7c7ca5", "latest": "sha256:e1646c12f18dcf88aa82b72d1d3810e3f3067494c821e2ed64d3232068a7901e", "11.0.3": "sha256:e1646c12f18dcf88aa82b72d1d3810e3f3067494c821e2ed64d3232068a7901e"}, "aliases": {"Cast-config": "/opt/view/bin/Cast-config", "CreateDOMDocument": "/opt/view/bin/CreateDOMDocument", "DOMCount": "/opt/view/bin/DOMCount", "DOMPrint": "/opt/view/bin/DOMPrint", "EnumVal": "/opt/view/bin/EnumVal", "Evaluator-config": "/opt/view/bin/Evaluator-config", "Exceptions-config": "/opt/view/bin/Exceptions-config", "GenericFunctions-config": "/opt/view/bin/GenericFunctions-config", "Geometry-config": "/opt/view/bin/Geometry-config", "Matrix-config": "/opt/view/bin/Matrix-config", "MemParse": "/opt/view/bin/MemParse", "PParse": "/opt/view/bin/PParse", "PSVIWriter": "/opt/view/bin/PSVIWriter", "Random-config": "/opt/view/bin/Random-config", "RandomObjects-config": "/opt/view/bin/RandomObjects-config", "Redirect": "/opt/view/bin/Redirect", "RefCount-config": "/opt/view/bin/RefCount-config", "SAX2Count": "/opt/view/bin/SAX2Count", "SAX2Print": "/opt/view/bin/SAX2Print", "SAXCount": "/opt/view/bin/SAXCount", "SAXPrint": "/opt/view/bin/SAXPrint", "SCMPrint": "/opt/view/bin/SCMPrint", "SEnumVal": "/opt/view/bin/SEnumVal", "StdInParse": "/opt/view/bin/StdInParse", "Units-config": "/opt/view/bin/Units-config", "Utility-config": "/opt/view/bin/Utility-config", "Vector-config": "/opt/view/bin/Vector-config", "XInclude": "/opt/view/bin/XInclude", "geant4-config": "/opt/view/bin/geant4-config", "geant4.csh": "/opt/view/bin/geant4.csh", "geant4.sh": "/opt/view/bin/geant4.sh"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/geant4.
Geant4 is a platform for the simulation of the passage of particles through matter using Monte Carlo methods.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/geant4
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/geant4:11.0.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/geant4/11.0.0
$ module help ghcr.io/autamus/geant4/11.0.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### geant4-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### geant4-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### geant4-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### geant4-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### geant4-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### geant4-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Cast-config

```bash
$ singularity exec <container> /opt/view/bin/Cast-config
$ podman run --it --rm --entrypoint /opt/view/bin/Cast-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/Cast-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CreateDOMDocument

```bash
$ singularity exec <container> /opt/view/bin/CreateDOMDocument
$ podman run --it --rm --entrypoint /opt/view/bin/CreateDOMDocument   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/CreateDOMDocument   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DOMCount

```bash
$ singularity exec <container> /opt/view/bin/DOMCount
$ podman run --it --rm --entrypoint /opt/view/bin/DOMCount   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/DOMCount   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DOMPrint

```bash
$ singularity exec <container> /opt/view/bin/DOMPrint
$ podman run --it --rm --entrypoint /opt/view/bin/DOMPrint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/DOMPrint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### EnumVal

```bash
$ singularity exec <container> /opt/view/bin/EnumVal
$ podman run --it --rm --entrypoint /opt/view/bin/EnumVal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/EnumVal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Evaluator-config

```bash
$ singularity exec <container> /opt/view/bin/Evaluator-config
$ podman run --it --rm --entrypoint /opt/view/bin/Evaluator-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/Evaluator-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Exceptions-config

```bash
$ singularity exec <container> /opt/view/bin/Exceptions-config
$ podman run --it --rm --entrypoint /opt/view/bin/Exceptions-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/Exceptions-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GenericFunctions-config

```bash
$ singularity exec <container> /opt/view/bin/GenericFunctions-config
$ podman run --it --rm --entrypoint /opt/view/bin/GenericFunctions-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/GenericFunctions-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Geometry-config

```bash
$ singularity exec <container> /opt/view/bin/Geometry-config
$ podman run --it --rm --entrypoint /opt/view/bin/Geometry-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/Geometry-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Matrix-config

```bash
$ singularity exec <container> /opt/view/bin/Matrix-config
$ podman run --it --rm --entrypoint /opt/view/bin/Matrix-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/Matrix-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MemParse

```bash
$ singularity exec <container> /opt/view/bin/MemParse
$ podman run --it --rm --entrypoint /opt/view/bin/MemParse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/MemParse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PParse

```bash
$ singularity exec <container> /opt/view/bin/PParse
$ podman run --it --rm --entrypoint /opt/view/bin/PParse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/PParse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PSVIWriter

```bash
$ singularity exec <container> /opt/view/bin/PSVIWriter
$ podman run --it --rm --entrypoint /opt/view/bin/PSVIWriter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/PSVIWriter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Random-config

```bash
$ singularity exec <container> /opt/view/bin/Random-config
$ podman run --it --rm --entrypoint /opt/view/bin/Random-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/Random-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RandomObjects-config

```bash
$ singularity exec <container> /opt/view/bin/RandomObjects-config
$ podman run --it --rm --entrypoint /opt/view/bin/RandomObjects-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/RandomObjects-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Redirect

```bash
$ singularity exec <container> /opt/view/bin/Redirect
$ podman run --it --rm --entrypoint /opt/view/bin/Redirect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/Redirect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RefCount-config

```bash
$ singularity exec <container> /opt/view/bin/RefCount-config
$ podman run --it --rm --entrypoint /opt/view/bin/RefCount-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/RefCount-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SAX2Count

```bash
$ singularity exec <container> /opt/view/bin/SAX2Count
$ podman run --it --rm --entrypoint /opt/view/bin/SAX2Count   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/SAX2Count   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SAX2Print

```bash
$ singularity exec <container> /opt/view/bin/SAX2Print
$ podman run --it --rm --entrypoint /opt/view/bin/SAX2Print   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/SAX2Print   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SAXCount

```bash
$ singularity exec <container> /opt/view/bin/SAXCount
$ podman run --it --rm --entrypoint /opt/view/bin/SAXCount   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/SAXCount   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SAXPrint

```bash
$ singularity exec <container> /opt/view/bin/SAXPrint
$ podman run --it --rm --entrypoint /opt/view/bin/SAXPrint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/SAXPrint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SCMPrint

```bash
$ singularity exec <container> /opt/view/bin/SCMPrint
$ podman run --it --rm --entrypoint /opt/view/bin/SCMPrint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/SCMPrint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SEnumVal

```bash
$ singularity exec <container> /opt/view/bin/SEnumVal
$ podman run --it --rm --entrypoint /opt/view/bin/SEnumVal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/SEnumVal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### StdInParse

```bash
$ singularity exec <container> /opt/view/bin/StdInParse
$ podman run --it --rm --entrypoint /opt/view/bin/StdInParse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/StdInParse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Units-config

```bash
$ singularity exec <container> /opt/view/bin/Units-config
$ podman run --it --rm --entrypoint /opt/view/bin/Units-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/Units-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Utility-config

```bash
$ singularity exec <container> /opt/view/bin/Utility-config
$ podman run --it --rm --entrypoint /opt/view/bin/Utility-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/Utility-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Vector-config

```bash
$ singularity exec <container> /opt/view/bin/Vector-config
$ podman run --it --rm --entrypoint /opt/view/bin/Vector-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/Vector-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### XInclude

```bash
$ singularity exec <container> /opt/view/bin/XInclude
$ podman run --it --rm --entrypoint /opt/view/bin/XInclude   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/XInclude   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geant4-config

```bash
$ singularity exec <container> /opt/view/bin/geant4-config
$ podman run --it --rm --entrypoint /opt/view/bin/geant4-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/geant4-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geant4.csh

```bash
$ singularity exec <container> /opt/view/bin/geant4.csh
$ podman run --it --rm --entrypoint /opt/view/bin/geant4.csh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/geant4.csh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geant4.sh

```bash
$ singularity exec <container> /opt/view/bin/geant4.sh
$ podman run --it --rm --entrypoint /opt/view/bin/geant4.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/geant4.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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