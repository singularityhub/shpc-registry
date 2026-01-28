---
layout: container
name:  "jupyter/pyspark-notebook"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/jupyter/pyspark-notebook/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/jupyter/pyspark-notebook/container.yaml"
updated_at: "2026-01-28 03:49:17.573425"
latest: "2023-10-20"
container_url: "https://hub.docker.com/r/jupyter/pyspark-notebook"
aliases:
 - "run-notebook"
versions:
 - "4.0"
 - "latest"
 - "2022-04-05"
 - "2022-03-28"
 - "2022-02-28"
 - "2022-01-31"
 - "2021-12-27"
 - "2022-04-25"
 - "2022-05-31"
 - "2022-06-27"
 - "2022-08-23"
 - "2022-07-27"
 - "2022-08-29"
 - "2022-09-30"
 - "2022-11-15"
 - "2022-10-31"
 - "2022-12-15"
 - "2022-11-28"
 - "2023-01-16"
 - "2022-12-30"
 - "2023-02-17"
 - "2023-01-30"
 - "2023-03-13"
 - "2023-02-28"
 - "2023-04-17"
 - "2023-03-27"
 - "2023-05-15"
 - "2023-04-27"
 - "2023-06-13"
 - "2023-05-30"
 - "2023-07-17"
 - "2023-06-29"
 - "2023-08-14"
 - "2023-07-31"
 - "2023-09-16"
 - "2023-08-28"
 - "2023-10-17"
 - "2023-09-25"
 - "2023-10-20"
description: "Jupyter Pyspark Notebook from https://github.com/jupyter/docker-stacks"
config: {"docker": "jupyter/pyspark-notebook", "url": "https://hub.docker.com/r/jupyter/pyspark-notebook", "maintainer": "@vsoch", "description": "Jupyter Pyspark Notebook from https://github.com/jupyter/docker-stacks", "latest": {"2023-10-20": "sha256:58377aaa152b741e244f201679f96d909a024ea337088cc276b0ee32ab3f076f"}, "tags": {"4.0": "sha256:2aa9a0183bcfe80cd9e2a6c0a52d797bd5b67d1e2db9437c7345c2404b5a86c1", "latest": "sha256:58377aaa152b741e244f201679f96d909a024ea337088cc276b0ee32ab3f076f", "2022-04-05": "sha256:69ce4a6eaff98d5129fd5f76d992f836371752b0bab8567610d16bb1bb32ea43", "2022-03-28": "sha256:4bd42fd3182bcb70feaaf14876bfb7a5658961438acc79fe552baea646a4be3d", "2022-02-28": "sha256:13186f8f50347924656e96eb0b36dbc0e7b8aa5c69f2594c4b21c45ac0146300", "2022-01-31": "sha256:cc0b2ad428aef8ed8a4557888b2fb2b50ab125ba6eb1fcb58642d270edd9d60b", "2021-12-27": "sha256:8c45b68c6c19329a9091fd3e7e1afc7594fa0b240fb74c2230433a9c2466e968", "2022-04-25": "sha256:afc64f790d390a9b3ffc1f4847c7e077e90e92f098c0b2c34bb1ed74e101fba0", "2022-05-31": "sha256:98cbb6331e50005429915dfcd4972d6f0e97cd29371122e7ec5649c11a84b048", "2022-06-27": "sha256:f638168ca91d7c9f7f9999b0a384390ea0a46385aac223b6000a439c486a7260", "2022-08-23": "sha256:101620247291375b8f736121f81d7d9ce2b4a3b45db6ba00857506c7b52f5e2e", "2022-07-27": "sha256:9dd0932e05c5a0458494fe84fe80aa47c5f48dc92d0b5e41c5b292ebab6898a8", "2022-08-29": "sha256:650034e33aa985f3924cb8ad09f944eb1040e474781d34b6027e6d69732626e5", "2022-09-30": "sha256:6491f91c18ad888f9efb145cf97f3e848ceffdacf6932298fde101d7efe36067", "2022-11-15": "sha256:7e410638782b0e8cb838480d4dd2552e2731f77559bd6ce56a0186f7ea9afdc5", "2022-10-31": "sha256:5d0f7aab367b6734495d9f7642f4b0066d48280cfb61ff36061fd5ec4f69b232", "2022-12-15": "sha256:bfa91616dc9e2961c62cdce0e0aaf6fb5a5b3a6cc7a6e9a2393a607876a98ae8", "2022-11-28": "sha256:cf602da619816b97fdaeab1abe7792c1467f492b758cf2a24834c3bf425f4429", "2023-01-16": "sha256:64f7c95ecc614db205976c3128d951caae4bb8c8f9854bddb2b8bdebbe47c2cf", "2022-12-30": "sha256:99add601123e719cb0cc009266ddbaeb490bfdbc8c7f4327e38301ce9c35663b", "2023-02-17": "sha256:f68a473bc13ce8cb2c5c42aebdd553a01e695bc4438e50e5c374a607b84b2bd5", "2023-01-30": "sha256:5bea073966208d6f7ff044f64daadfa50812cbfda39e902a3de4a92fbff780df", "2023-03-13": "sha256:68a8cd2bd69d4584b95729b7c8aee5483790ca91621fa7dbaf755d9d65da6644", "2023-02-28": "sha256:53853653ffa1b391f032762d1fabb7471c2f6dc2cdf580a9465d39d830a88d02", "2023-04-17": "sha256:a4ef9b9ce25d397142f7bcbda7d978c622940104f929b7befca225262889be59", "2023-03-27": "sha256:d5b8cd3aa5d84d408720779e294007a9a447e78071b1c4e93a69e36d7a84028a", "2023-05-15": "sha256:64ec7db4ea5b4f166d1240ba962a0d57bd3234ba022200ae0f8582e742887533", "2023-04-27": "sha256:a653fa15943f216aaa09a751f3bb1e5f9cfc377f97e76da2838b369a90dcca7e", "2023-06-13": "sha256:a192d585bc953702b4f49cb912799212146c811ca9ae85ea8c5f09d7d741da60", "2023-05-30": "sha256:ee0c154cb39670ee932fc8a0fab19351f00a10a46474afd1425396b7788dae96", "2023-07-17": "sha256:7b49f0c6e708492de6b35a81bd7a65fd81882c63a9958f97bcb7638c1b93385e", "2023-06-29": "sha256:4b1cf332a6e2e36695a7624e1074246ac95dd8497cb2cf5c3773030c73fb0535", "2023-08-14": "sha256:40c277399da9f7aa334e4465610bd2e04b739580649b7df263083132864b71f4", "2023-07-31": "sha256:397d37c48c951514f3474580abe21423c838209acd62ea991c527dc9437b08d4", "2023-09-16": "sha256:b105b4786e7941a63027510258014895cad872f6f948ed44ada685d9d4825eed", "2023-08-28": "sha256:79483fb5d0e2f6539c83f83d8e15462e8a2cce3034bf9b39e10879234652a7fd", "2023-10-17": "sha256:f5b0f13967d986bd2b48327ad7e1e12da6aa8327337537a3403f63e6ee1828ad", "2023-09-25": "sha256:af0af59428334e69228a0ae524a21fadee870333a3ee16f654e2d60d9a82705c", "2023-10-20": "sha256:58377aaa152b741e244f201679f96d909a024ea337088cc276b0ee32ab3f076f"}, "aliases": [{"name": "run-notebook", "command": "jupyter notebook --no-browser --port=$(shuf -i 2000-65000 -n 1) --ip 0.0.0.0"}]}
---

This module is a singularity container wrapper for jupyter/pyspark-notebook.
Jupyter Pyspark Notebook from https://github.com/jupyter/docker-stacks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install jupyter/pyspark-notebook
```

Or a specific version:

```bash
$ shpc install jupyter/pyspark-notebook:2023-10-20
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load jupyter/pyspark-notebook/2023-10-20
$ module help jupyter/pyspark-notebook/2023-10-20
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pyspark-notebook-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pyspark-notebook-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pyspark-notebook-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pyspark-notebook-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pyspark-notebook-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pyspark-notebook-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### run-notebook

```bash
$ singularity exec <container> jupyter notebook --no-browser --port=$(shuf -i 2000-65000 -n 1) --ip 0.0.0.0
$ podman run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
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