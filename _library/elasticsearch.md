---
layout: container
name:  "elasticsearch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/elasticsearch/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/elasticsearch/container.yaml"
updated_at: "2023-11-20 03:18:40.617728"
latest: "8.10.2"
container_url: "https://hub.docker.com/_/elasticsearch"
aliases:
 - "elasticsearch"
 - "elasticsearch-certgen"
 - "elasticsearch-certutil"
 - "elasticsearch-cli"
 - "elasticsearch-croneval"
 - "elasticsearch-env"
 - "elasticsearch-env-from-file"
 - "elasticsearch-keystore"
 - "elasticsearch-migrate"
 - "elasticsearch-node"
 - "elasticsearch-plugin"
 - "elasticsearch-saml-metadata"
 - "elasticsearch-setup-passwords"
 - "elasticsearch-shard"
 - "elasticsearch-sql-cli"
 - "elasticsearch-sql-cli-7.12.0.jar"
 - "elasticsearch-syskeygen"
 - "elasticsearch-users"
versions:
 - "7.12.0"
 - "7.12.1"
 - "7.13.1"
 - "7.13.2"
 - "7.13.3"
 - "7.14.0"
 - "7.14.2"
 - "7.16.2"
 - "7.16.3"
 - "8.0.0"
 - "8.1.2"
 - "8.0.1"
 - "7.17.2"
 - "8.1.3"
 - "7.17.3"
 - "8.2.2"
 - "7.17.4"
 - "8.3.1"
 - "8.2.3"
 - "7.17.5"
 - "8.4.0"
 - "8.3.3"
 - "8.4.1"
 - "8.4.2"
 - "8.5.3"
 - "8.4.3"
 - "8.6.0"
 - "8.6.1"
 - "8.6.2"
 - "8.7.0"
 - "8.7.1"
 - "8.8.1"
 - "8.10.1"
 - "8.9.2"
 - "8.8.2"
 - "8.10.2"
description: "Elasticsearch is a powerful open source search and analytics engine that makes data easy to explore."
config: {"docker": "elasticsearch", "url": "https://hub.docker.com/_/elasticsearch", "maintainer": "@vsoch", "description": "Elasticsearch is a powerful open source search and analytics engine that makes data easy to explore.", "latest": {"8.10.2": "sha256:53efb4ba72e1c71c8223ee8d8de6537e8d992ad6cc8fcdf5dd944be93b6ab814"}, "tags": {"7.12.0": "sha256:383e9fb572f3ca2fdef5ba2edb0dae2c467736af96aba2c193722aa0c08ca7ec", "7.12.1": "sha256:622f854572780281bc85b5fde33be27e99670941ed8b7eea5ba4aaf533fa64ec", "7.13.1": "sha256:39ffcfec57f570dd113d13c69df8491ad013750c225b72e872284ea08d06bbcb", "7.13.2": "sha256:6d2b3d9cf0de69c708919a20f38a11590e9ba73587b81733e4faa1cb032ee56b", "7.13.3": "sha256:759533051d0d5c67f7b09c8655ea00af3a8f15f98e2df4ea76ff2b47967488a5", "7.14.0": "sha256:81c126e4eddbc5576285670cb3e23d7ef7892ee5e757d6d9ba870b6fe99f1219", "7.14.2": "sha256:f05ab7f4d2aa5040813a0ea4eb76fa99bb31459937a4539efe2f2c2dbb2109fb", "7.16.2": "sha256:fe7ae76ec33e1222ece5216e3a9c6346999a73d3fb65256abb01638758db4b5d", "7.16.3": "sha256:de5474d051409e8222eee30c82ef299f3f3c97bb339bbd19c314178db659f7b4", "8.0.0": "sha256:19f79b36495507ec53867ab40acaae448a9baa7820fb843be8cb5ede670bac5b", "8.1.2": "sha256:9785077d3781c0049a7fb9488a3b3a6d40bf529c105c8f3530533701ce00e602", "8.0.1": "sha256:082149d7e8b395ac569d3a019afc4169dfb7d8edf9e7d4fa83463e60d64387a4", "7.17.2": "sha256:f51e653b5dfca16afef88d870b697e087e4b562c63c3272d6e8c3c92657110d9", "8.1.3": "sha256:cc4e15f02c76d64cf2cf07a031ba31fc33e7c55bf48d0088ba06f3edc95c2e12", "7.17.3": "sha256:5e6ac15bf6a57c42fa702a647c13749b1249c89e59be8f654f61a3feade9dc47", "8.2.2": "sha256:8c666cb1e76650306655b67644a01663f9c7a5422b2c51dd570524267f11ce3d", "7.17.4": "sha256:529b3cfec4354beda158c6c7f2f8015cbdc9432a48c1d63e824d6fd728f30db2", "8.3.1": "sha256:bad94c9a0180cb4e6e81f09da4d510a761fec9fcba92c34af703233d3b615aea", "8.2.3": "sha256:f1363868e19aa721355f387a8e79a33496c56fb525d37bc27e032a5c1e540b1e", "7.17.5": "sha256:473c4c41654e5cf201a10291a38646eb3c4019a2c88532a2b66468d2e851b473", "8.4.0": "sha256:8e25bf1dcb35c3af54607dc0619ec3fbabc58830d3db856624bb1637b11a6e42", "8.3.3": "sha256:966ce0b0266b41dafb4739c4ce18fb7ed434723d0e9f21d9520d4e6f2cdda2e1", "8.4.1": "sha256:7dd81b0af4aa916cf58373d5befaad56f89b96dd5582ced9f63879ed2650802c", "8.4.2": "sha256:2145d5f6bf5bd623ec49346dea619a35224062532ca762a7c150115e9bca20b8", "8.5.3": "sha256:47c8ece048c9625b72b2f3fb6ea5eda5c6e918afe80f6bf5d474160cb28867fc", "8.4.3": "sha256:bb72a5788e156171b111d2fc21825d007f235c3314295aa86d0ef500678923bd", "8.6.0": "sha256:12d0ff50b96a53d2a8e103ba2e0e69187babc3dcf8bdc88788d019cdebb75c0c", "8.6.1": "sha256:6242ee491ce3bbdb60543ae31e095630da00a413fa7d3885966a0642734bb69d", "8.6.2": "sha256:93bc71907ca0e6e3b4f181e0dc850b90bb6cb2686c2778def0b8542398983c28", "8.7.0": "sha256:53e51bde90897d77fdbc53677331504bbbdcc788cb7aadcd8fe707a77733dbb5", "8.7.1": "sha256:160814e5972521291420c29edf4c0348b8591ac9235156f0dbf34befcf362825", "8.8.1": "sha256:e31753d052509353f99be86892bf5c65a070805aadbb295d1b3128163061ea68", "8.10.1": "sha256:097d6efc50c7a7eb2201b3f95be37f88217fefb5a3fef1548d63383f9201f862", "8.9.2": "sha256:38082e945768e8e98fc0d828c810baf0b63d58ddc9059db2a62e4c293e44e817", "8.8.2": "sha256:acb934176519afa01f195e06b6085a5159401be37cdd70c2fbcd04890581e41b", "8.10.2": "sha256:53efb4ba72e1c71c8223ee8d8de6537e8d992ad6cc8fcdf5dd944be93b6ab814"}, "aliases": {"elasticsearch": "/usr/share/elasticsearch/bin/elasticsearch", "elasticsearch-certgen": "/usr/share/elasticsearch/bin/elasticsearch-certgen", "elasticsearch-certutil": "/usr/share/elasticsearch/bin/elasticsearch-certutil", "elasticsearch-cli": "/usr/share/elasticsearch/bin/elasticsearch-cli", "elasticsearch-croneval": "/usr/share/elasticsearch/bin/elasticsearch-croneval", "elasticsearch-env": "/usr/share/elasticsearch/bin/elasticsearch-env", "elasticsearch-env-from-file": "/usr/share/elasticsearch/bin/elasticsearch-env-from-file", "elasticsearch-keystore": "/usr/share/elasticsearch/bin/elasticsearch-keystore", "elasticsearch-migrate": "/usr/share/elasticsearch/bin/elasticsearch-migrate", "elasticsearch-node": "/usr/share/elasticsearch/bin/elasticsearch-node", "elasticsearch-plugin": "/usr/share/elasticsearch/bin/elasticsearch-plugin", "elasticsearch-saml-metadata": "/usr/share/elasticsearch/bin/elasticsearch-saml-metadata", "elasticsearch-setup-passwords": "/usr/share/elasticsearch/bin/elasticsearch-setup-passwords", "elasticsearch-shard": "/usr/share/elasticsearch/bin/elasticsearch-shard", "elasticsearch-sql-cli": "/usr/share/elasticsearch/bin/elasticsearch-sql-cli", "elasticsearch-sql-cli-7.12.0.jar": "java jar /usr/share/elasticsearch/bin/elasticsearch-sql-cli-7.12.0.jar", "elasticsearch-syskeygen": "/usr/share/elasticsearch/bin/elasticsearch-syskeygen", "elasticsearch-users": "/usr/share/elasticsearch/bin/elasticsearch-users"}}
---

This module is a singularity container wrapper for elasticsearch.
Elasticsearch is a powerful open source search and analytics engine that makes data easy to explore.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install elasticsearch
```

Or a specific version:

```bash
$ shpc install elasticsearch:8.10.2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load elasticsearch/8.10.2
$ module help elasticsearch/8.10.2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### elasticsearch-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### elasticsearch-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### elasticsearch-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### elasticsearch-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### elasticsearch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### elasticsearch-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### elasticsearch

```bash
$ singularity exec <container> /usr/share/elasticsearch/bin/elasticsearch
$ podman run --it --rm --entrypoint /usr/share/elasticsearch/bin/elasticsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/share/elasticsearch/bin/elasticsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticsearch-certgen

```bash
$ singularity exec <container> /usr/share/elasticsearch/bin/elasticsearch-certgen
$ podman run --it --rm --entrypoint /usr/share/elasticsearch/bin/elasticsearch-certgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/share/elasticsearch/bin/elasticsearch-certgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticsearch-certutil

```bash
$ singularity exec <container> /usr/share/elasticsearch/bin/elasticsearch-certutil
$ podman run --it --rm --entrypoint /usr/share/elasticsearch/bin/elasticsearch-certutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/share/elasticsearch/bin/elasticsearch-certutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticsearch-cli

```bash
$ singularity exec <container> /usr/share/elasticsearch/bin/elasticsearch-cli
$ podman run --it --rm --entrypoint /usr/share/elasticsearch/bin/elasticsearch-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/share/elasticsearch/bin/elasticsearch-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticsearch-croneval

```bash
$ singularity exec <container> /usr/share/elasticsearch/bin/elasticsearch-croneval
$ podman run --it --rm --entrypoint /usr/share/elasticsearch/bin/elasticsearch-croneval   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/share/elasticsearch/bin/elasticsearch-croneval   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticsearch-env

```bash
$ singularity exec <container> /usr/share/elasticsearch/bin/elasticsearch-env
$ podman run --it --rm --entrypoint /usr/share/elasticsearch/bin/elasticsearch-env   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/share/elasticsearch/bin/elasticsearch-env   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticsearch-env-from-file

```bash
$ singularity exec <container> /usr/share/elasticsearch/bin/elasticsearch-env-from-file
$ podman run --it --rm --entrypoint /usr/share/elasticsearch/bin/elasticsearch-env-from-file   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/share/elasticsearch/bin/elasticsearch-env-from-file   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticsearch-keystore

```bash
$ singularity exec <container> /usr/share/elasticsearch/bin/elasticsearch-keystore
$ podman run --it --rm --entrypoint /usr/share/elasticsearch/bin/elasticsearch-keystore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/share/elasticsearch/bin/elasticsearch-keystore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticsearch-migrate

```bash
$ singularity exec <container> /usr/share/elasticsearch/bin/elasticsearch-migrate
$ podman run --it --rm --entrypoint /usr/share/elasticsearch/bin/elasticsearch-migrate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/share/elasticsearch/bin/elasticsearch-migrate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticsearch-node

```bash
$ singularity exec <container> /usr/share/elasticsearch/bin/elasticsearch-node
$ podman run --it --rm --entrypoint /usr/share/elasticsearch/bin/elasticsearch-node   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/share/elasticsearch/bin/elasticsearch-node   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticsearch-plugin

```bash
$ singularity exec <container> /usr/share/elasticsearch/bin/elasticsearch-plugin
$ podman run --it --rm --entrypoint /usr/share/elasticsearch/bin/elasticsearch-plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/share/elasticsearch/bin/elasticsearch-plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticsearch-saml-metadata

```bash
$ singularity exec <container> /usr/share/elasticsearch/bin/elasticsearch-saml-metadata
$ podman run --it --rm --entrypoint /usr/share/elasticsearch/bin/elasticsearch-saml-metadata   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/share/elasticsearch/bin/elasticsearch-saml-metadata   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticsearch-setup-passwords

```bash
$ singularity exec <container> /usr/share/elasticsearch/bin/elasticsearch-setup-passwords
$ podman run --it --rm --entrypoint /usr/share/elasticsearch/bin/elasticsearch-setup-passwords   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/share/elasticsearch/bin/elasticsearch-setup-passwords   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticsearch-shard

```bash
$ singularity exec <container> /usr/share/elasticsearch/bin/elasticsearch-shard
$ podman run --it --rm --entrypoint /usr/share/elasticsearch/bin/elasticsearch-shard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/share/elasticsearch/bin/elasticsearch-shard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticsearch-sql-cli

```bash
$ singularity exec <container> /usr/share/elasticsearch/bin/elasticsearch-sql-cli
$ podman run --it --rm --entrypoint /usr/share/elasticsearch/bin/elasticsearch-sql-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/share/elasticsearch/bin/elasticsearch-sql-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticsearch-sql-cli-7.12.0.jar

```bash
$ singularity exec <container> java jar /usr/share/elasticsearch/bin/elasticsearch-sql-cli-7.12.0.jar
$ podman run --it --rm --entrypoint java   -v ${PWD} -w ${PWD} <container> -c "jar /usr/share/elasticsearch/bin/elasticsearch-sql-cli-7.12.0.jar $@"
$ docker run --it --rm --entrypoint java   -v ${PWD} -w ${PWD} <container> -c "jar /usr/share/elasticsearch/bin/elasticsearch-sql-cli-7.12.0.jar $@"
```


#### elasticsearch-syskeygen

```bash
$ singularity exec <container> /usr/share/elasticsearch/bin/elasticsearch-syskeygen
$ podman run --it --rm --entrypoint /usr/share/elasticsearch/bin/elasticsearch-syskeygen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/share/elasticsearch/bin/elasticsearch-syskeygen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticsearch-users

```bash
$ singularity exec <container> /usr/share/elasticsearch/bin/elasticsearch-users
$ podman run --it --rm --entrypoint /usr/share/elasticsearch/bin/elasticsearch-users   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/share/elasticsearch/bin/elasticsearch-users   -v ${PWD} -w ${PWD} <container> -c " $@"
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