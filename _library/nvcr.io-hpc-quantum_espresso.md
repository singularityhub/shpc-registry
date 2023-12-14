---
layout: container
name:  "nvcr.io/hpc/quantum_espresso"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/nvcr.io/hpc/quantum_espresso/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/nvcr.io/hpc/quantum_espresso/container.yaml"
updated_at: "2023-12-14 03:43:23.816875"
latest: "sha256-7792684f22eb7ebc718fa427e2f617d6a107787e4bff493b8a17de6c1381403c.sbom"
container_url: "https://ngc.nvidia.com/catalog/containers/hpc:quantum_espresso/tags"

versions:
 - "v6.7"
 - "qe-6.8"
 - "qe-7.0"
 - "qe-7.1"
 - "sha256-7792684f22eb7ebc718fa427e2f617d6a107787e4bff493b8a17de6c1381403c.sbom"
 - "sha256-cf59868f2a69a3dd978f548d900a7c14064cee09626b93b7bdaae144ecb17ce6.sbom"
 - "sha256-6702ec42e497dd21faf291c8104cc580301425a459760a8b392555d90d3e2cfc.vex"
 - "sha256-878c35fe26b3f350c046b4c0af6ce37a6c52da73218e943e7aaaed5387fa8a25.sbom"
 - "sha256-352db5b01c148b061c057a3452df1c72cf7e27ca022e2b4b29a2e3c367f3b883.sbom"
description: "Quantum ESPRESSO is an integrated suite of Open-Source computer codes for electronic-structure calculations and materials modeling at the nanoscale based on density-functional theory, plane waves, and pseudopotentials."
config: {"docker": "nvcr.io/hpc/quantum_espresso", "url": "https://ngc.nvidia.com/catalog/containers/hpc:quantum_espresso/tags", "maintainer": "@vsoch", "description": "Quantum ESPRESSO is an integrated suite of Open-Source computer codes for electronic-structure calculations and materials modeling at the nanoscale based on density-functional theory, plane waves, and pseudopotentials.", "latest": {"sha256-7792684f22eb7ebc718fa427e2f617d6a107787e4bff493b8a17de6c1381403c.sbom": "sha256:90f9de3d4de983883f417593560b2720747233a7ac1d527a6c8e1ee94ec796e9"}, "tags": {"v6.7": "sha256:fdcea13eec98f48af813f172be42a40adf4e856d07cfb4ee1fc584d5c4a8f0f9", "qe-6.8": "sha256:1db6a3eae9baa8cbb6c72f227c14d48fd8a8b2548f021c10764608a321525de8", "qe-7.0": "sha256:e117f9df9868b7d7908fabc951719d8bf4a450ef7a9a01cf2e0ed5ab3f2b9651", "qe-7.1": "sha256:e525848fd411302f1e941b34f145a988a0ea2d300e14c93d3deec291c4c88edc", "sha256-7792684f22eb7ebc718fa427e2f617d6a107787e4bff493b8a17de6c1381403c.sbom": "sha256:90f9de3d4de983883f417593560b2720747233a7ac1d527a6c8e1ee94ec796e9", "sha256-cf59868f2a69a3dd978f548d900a7c14064cee09626b93b7bdaae144ecb17ce6.sbom": "sha256:7c509ce57de0d8a402b928b4444bb570e08c4879eb2f7b23d039f00fa788feeb", "sha256-6702ec42e497dd21faf291c8104cc580301425a459760a8b392555d90d3e2cfc.vex": "sha256:b809fa5a124d5f84324644b2a773e1475ef0ffceccc98a369e2a5e89acf4c4ec", "sha256-878c35fe26b3f350c046b4c0af6ce37a6c52da73218e943e7aaaed5387fa8a25.sbom": "sha256:cda1c25b7ffe60b1bffff2957002e246502a07e73031f2d327bf90653295e828", "sha256-352db5b01c148b061c057a3452df1c72cf7e27ca022e2b4b29a2e3c367f3b883.sbom": "sha256:bd39b5e60e7e9cdea4cc7411e4bee4769652b998e4506795a949611b272b0f2c"}, "filter": ["v*"], "features": {"gpu": true}}
---

This module is a singularity container wrapper for nvcr.io/hpc/quantum_espresso.
Quantum ESPRESSO is an integrated suite of Open-Source computer codes for electronic-structure calculations and materials modeling at the nanoscale based on density-functional theory, plane waves, and pseudopotentials.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install nvcr.io/hpc/quantum_espresso
```

Or a specific version:

```bash
$ shpc install nvcr.io/hpc/quantum_espresso:sha256-7792684f22eb7ebc718fa427e2f617d6a107787e4bff493b8a17de6c1381403c.sbom
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load nvcr.io/hpc/quantum_espresso/sha256-7792684f22eb7ebc718fa427e2f617d6a107787e4bff493b8a17de6c1381403c.sbom
$ module help nvcr.io/hpc/quantum_espresso/sha256-7792684f22eb7ebc718fa427e2f617d6a107787e4bff493b8a17de6c1381403c.sbom
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### quantum_espresso-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### quantum_espresso-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### quantum_espresso-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### quantum_espresso-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### quantum_espresso-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### quantum_espresso-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### quantum_espresso

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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