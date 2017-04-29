#!/bin/bash

set -eu

CURRENT=$(cd $(dirname $0) && pwd)

readonly PROM="$CURRENT/raspi.prom"

function get_raspi_data() {
  local _temperature=$(vcgencmd measure_temp | sed -e "s/^temp=\([0-9]\+\.[0-9]\+\)'C/\1/g")
  local _volt=$(vcgencmd measure_volts | sed -e "s/^volt=\([0-9]\+\.[0-9]\+\)V$/\1/g")
  local _mem_arm=$(vcgencmd get_mem arm | sed -e "s/^arm=\([0-9]\+\)M$/\1/g")
  local _mem_gpu=$(vcgencmd get_mem gpu | sed -e "s/^gpu=\([0-9]\+\)M$/\1/g")

  echo "node_raspi_temperature ${_temperature}" >> ${PROM}.$$
  echo "node_raspi_volt ${_volt}" >> ${PROM}.$$
  echo "node_raspi_arm_memory ${_mem_arm}" >> ${PROM}.$$
  echo "node_raspi_gpu_memory ${_mem_gpu}" >> ${PROM}.$$
}

function finisher() {
  mv ${PROM}.$$ ${PROM}
}


get_raspi_data

finisher
