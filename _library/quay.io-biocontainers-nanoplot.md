---
layout: container
name:  "quay.io/biocontainers/nanoplot"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nanoplot/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nanoplot/container.yaml"
updated_at: "2025-03-18 03:17:51.395332"
latest: "1.44.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/nanoplot"
aliases:
 - "NanoPlot"
 - "pauvre"
 - "createfontdatachunk.py"
 - "enhancer.py"
 - "explode.py"
 - "gifmaker.py"
 - "painter.py"
 - "player.py"
 - "thresholder.py"
 - "viewer.py"
 - "pilconvert.py"
 - "pildriver.py"
versions:
 - "1.8.1--py36_0"
 - "1.36.1--pyhdfd78af_0"
 - "1.35.5--pyhdfd78af_0"
 - "1.32.1--py_0"
 - "1.31.0--py_0"
 - "1.30.1--py_0"
 - "1.43.0--pyhdfd78af_1"
 - "1.42.0--pyhdfd78af_0"
 - "1.41.6--pyhdfd78af_0"
 - "1.40.2--pyhdfd78af_0"
 - "1.39.0--pyhdfd78af_0"
 - "1.44.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for nanoplot"
config: {"url": "https://biocontainers.pro/tools/nanoplot", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nanoplot", "latest": {"1.44.1--pyhdfd78af_0": "sha256:85f6fc3c9cd76fd51c4bcf457ad46ce6ad6b868b88f2983c5e4fcfe86f44190c"}, "tags": {"1.8.1--py36_0": "sha256:b73d5b3c734675e473b3ecea4cd72df9f224877b51f8f8e68693a10b98dc733f", "1.36.1--pyhdfd78af_0": "sha256:89592cc9e68e6d4f95d7695f7c70841a638013a4d210a139f0608ded1902af40", "1.35.5--pyhdfd78af_0": "sha256:2218e1ddeddd55857c36bb77d20533ef16fcd45e5f6126b9f895c219daa2c3f0", "1.32.1--py_0": "sha256:03ba69a3f1b359c9cdbaa1275add8cbbe1749908a5c9cc81d81c0498a1536bb8", "1.31.0--py_0": "sha256:949bd5be4f6ce9cb4d0e919751a02cfb1b5108428e2a9cae3c73e2279891183e", "1.30.1--py_0": "sha256:a99cdf02d901dbe170640a709c1529fb94a520101addb7c7e5cc11eb559a3fcf", "1.43.0--pyhdfd78af_1": "sha256:ead345e36f33aac4f8062e0635baa3c1ba047708680921c37fb53a531d6587cf", "1.42.0--pyhdfd78af_0": "sha256:8eb31b6d172a997cb9bc5b00efc36e0376829dcb7bf3b64fd7490608f2b64cbf", "1.41.6--pyhdfd78af_0": "sha256:06e4ce10ed6c0cbea939eb8fe9df9d9e457734b9fbc872469c2c82805822a5a5", "1.40.2--pyhdfd78af_0": "sha256:8caeeac4d2358a7ec0299a5d04023b1cf04eecc2b2beb963be52c8f9cf99198f", "1.39.0--pyhdfd78af_0": "sha256:75c8f61b1b2c6a8c62c9e622e088b98f3298ac6aa136d9b259d89246295cd7cd", "1.44.1--pyhdfd78af_0": "sha256:85f6fc3c9cd76fd51c4bcf457ad46ce6ad6b868b88f2983c5e4fcfe86f44190c"}, "docker": "quay.io/biocontainers/nanoplot", "aliases": {"NanoPlot": "/usr/local/bin/NanoPlot", "pauvre": "/usr/local/bin/pauvre", "createfontdatachunk.py": "/usr/local/bin/createfontdatachunk.py", "enhancer.py": "/usr/local/bin/enhancer.py", "explode.py": "/usr/local/bin/explode.py", "gifmaker.py": "/usr/local/bin/gifmaker.py", "painter.py": "/usr/local/bin/painter.py", "player.py": "/usr/local/bin/player.py", "thresholder.py": "/usr/local/bin/thresholder.py", "viewer.py": "/usr/local/bin/viewer.py", "pilconvert.py": "/usr/local/bin/pilconvert.py", "pildriver.py": "/usr/local/bin/pildriver.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nanoplot.
shpc-registry automated BioContainers addition for nanoplot
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nanoplot
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nanoplot:1.44.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nanoplot/1.44.1--pyhdfd78af_0
$ module help quay.io/biocontainers/nanoplot/1.44.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nanoplot-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nanoplot-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nanoplot-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nanoplot-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nanoplot-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nanoplot-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### NanoPlot

```bash
$ singularity exec <container> /usr/local/bin/NanoPlot
$ podman run --it --rm --entrypoint /usr/local/bin/NanoPlot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/NanoPlot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pauvre

```bash
$ singularity exec <container> /usr/local/bin/pauvre
$ podman run --it --rm --entrypoint /usr/local/bin/pauvre   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pauvre   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### createfontdatachunk.py

```bash
$ singularity exec <container> /usr/local/bin/createfontdatachunk.py
$ podman run --it --rm --entrypoint /usr/local/bin/createfontdatachunk.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/createfontdatachunk.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### enhancer.py

```bash
$ singularity exec <container> /usr/local/bin/enhancer.py
$ podman run --it --rm --entrypoint /usr/local/bin/enhancer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/enhancer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### explode.py

```bash
$ singularity exec <container> /usr/local/bin/explode.py
$ podman run --it --rm --entrypoint /usr/local/bin/explode.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/explode.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifmaker.py

```bash
$ singularity exec <container> /usr/local/bin/gifmaker.py
$ podman run --it --rm --entrypoint /usr/local/bin/gifmaker.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifmaker.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### painter.py

```bash
$ singularity exec <container> /usr/local/bin/painter.py
$ podman run --it --rm --entrypoint /usr/local/bin/painter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/painter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### player.py

```bash
$ singularity exec <container> /usr/local/bin/player.py
$ podman run --it --rm --entrypoint /usr/local/bin/player.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/player.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### thresholder.py

```bash
$ singularity exec <container> /usr/local/bin/thresholder.py
$ podman run --it --rm --entrypoint /usr/local/bin/thresholder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/thresholder.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### viewer.py

```bash
$ singularity exec <container> /usr/local/bin/viewer.py
$ podman run --it --rm --entrypoint /usr/local/bin/viewer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/viewer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pilconvert.py

```bash
$ singularity exec <container> /usr/local/bin/pilconvert.py
$ podman run --it --rm --entrypoint /usr/local/bin/pilconvert.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pilconvert.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pildriver.py

```bash
$ singularity exec <container> /usr/local/bin/pildriver.py
$ podman run --it --rm --entrypoint /usr/local/bin/pildriver.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pildriver.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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