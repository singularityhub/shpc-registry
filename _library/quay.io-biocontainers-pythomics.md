---
layout: container
name:  "quay.io/biocontainers/pythomics"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pythomics/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pythomics/container.yaml"
updated_at: "2025-03-31 03:24:24.180776"
latest: "0.4.1--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/pythomics"
aliases:
 - "fastadigest.py"
 - "fastadigeststats.py"
 - "fastxTrimmer.py"
 - "featureCollapser.py"
 - "fetchOrfs.py"
 - "incorporateGFF.py"
 - "incorporateVCF.py"
 - "intersectFiles.py"
 - "junctionalReads.py"
 - "proteinInference.py"
 - "ptmSummary.py"
 - "xslt-config"
 - "xsltproc"
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
versions:
 - "0.3.46--pyh864c0ab_2"
 - "0.4.1--pyh7cba7a3_0"
description: "shpc-registry automated BioContainers addition for pythomics"
config: {"url": "https://biocontainers.pro/tools/pythomics", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pythomics", "latest": {"0.4.1--pyh7cba7a3_0": "sha256:261ca349b67c7309fffdc6dbf68cd97cf2f0f02427f5f03209d08224bd983b1c"}, "tags": {"0.3.46--pyh864c0ab_2": "sha256:f258a56bb40507ee691bd6b5f52ee4be9509b25561fa67e6b0e7296c0b1f240c", "0.4.1--pyh7cba7a3_0": "sha256:261ca349b67c7309fffdc6dbf68cd97cf2f0f02427f5f03209d08224bd983b1c"}, "docker": "quay.io/biocontainers/pythomics", "aliases": {"fastadigest.py": "/usr/local/bin/fastadigest.py", "fastadigeststats.py": "/usr/local/bin/fastadigeststats.py", "fastxTrimmer.py": "/usr/local/bin/fastxTrimmer.py", "featureCollapser.py": "/usr/local/bin/featureCollapser.py", "fetchOrfs.py": "/usr/local/bin/fetchOrfs.py", "incorporateGFF.py": "/usr/local/bin/incorporateGFF.py", "incorporateVCF.py": "/usr/local/bin/incorporateVCF.py", "intersectFiles.py": "/usr/local/bin/intersectFiles.py", "junctionalReads.py": "/usr/local/bin/junctionalReads.py", "proteinInference.py": "/usr/local/bin/proteinInference.py", "ptmSummary.py": "/usr/local/bin/ptmSummary.py", "xslt-config": "/usr/local/bin/xslt-config", "xsltproc": "/usr/local/bin/xsltproc", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pythomics.
shpc-registry automated BioContainers addition for pythomics
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pythomics
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pythomics:0.4.1--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pythomics/0.4.1--pyh7cba7a3_0
$ module help quay.io/biocontainers/pythomics/0.4.1--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pythomics-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pythomics-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pythomics-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pythomics-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pythomics-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pythomics-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastadigest.py

```bash
$ singularity exec <container> /usr/local/bin/fastadigest.py
$ podman run --it --rm --entrypoint /usr/local/bin/fastadigest.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastadigest.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastadigeststats.py

```bash
$ singularity exec <container> /usr/local/bin/fastadigeststats.py
$ podman run --it --rm --entrypoint /usr/local/bin/fastadigeststats.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastadigeststats.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastxTrimmer.py

```bash
$ singularity exec <container> /usr/local/bin/fastxTrimmer.py
$ podman run --it --rm --entrypoint /usr/local/bin/fastxTrimmer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastxTrimmer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### featureCollapser.py

```bash
$ singularity exec <container> /usr/local/bin/featureCollapser.py
$ podman run --it --rm --entrypoint /usr/local/bin/featureCollapser.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/featureCollapser.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetchOrfs.py

```bash
$ singularity exec <container> /usr/local/bin/fetchOrfs.py
$ podman run --it --rm --entrypoint /usr/local/bin/fetchOrfs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetchOrfs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### incorporateGFF.py

```bash
$ singularity exec <container> /usr/local/bin/incorporateGFF.py
$ podman run --it --rm --entrypoint /usr/local/bin/incorporateGFF.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/incorporateGFF.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### incorporateVCF.py

```bash
$ singularity exec <container> /usr/local/bin/incorporateVCF.py
$ podman run --it --rm --entrypoint /usr/local/bin/incorporateVCF.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/incorporateVCF.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intersectFiles.py

```bash
$ singularity exec <container> /usr/local/bin/intersectFiles.py
$ podman run --it --rm --entrypoint /usr/local/bin/intersectFiles.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intersectFiles.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### junctionalReads.py

```bash
$ singularity exec <container> /usr/local/bin/junctionalReads.py
$ podman run --it --rm --entrypoint /usr/local/bin/junctionalReads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/junctionalReads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proteinInference.py

```bash
$ singularity exec <container> /usr/local/bin/proteinInference.py
$ podman run --it --rm --entrypoint /usr/local/bin/proteinInference.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proteinInference.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ptmSummary.py

```bash
$ singularity exec <container> /usr/local/bin/ptmSummary.py
$ podman run --it --rm --entrypoint /usr/local/bin/ptmSummary.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ptmSummary.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xslt-config

```bash
$ singularity exec <container> /usr/local/bin/xslt-config
$ podman run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xsltproc

```bash
$ singularity exec <container> /usr/local/bin/xsltproc
$ podman run --it --rm --entrypoint /usr/local/bin/xsltproc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xsltproc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.8

```bash
$ singularity exec <container> /usr/local/bin/idle3.8
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.8

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.8
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8

```bash
$ singularity exec <container> /usr/local/bin/python3.8
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8-config

```bash
$ singularity exec <container> /usr/local/bin/python3.8-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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