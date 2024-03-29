. ./path.sh

. utils/parse_options.sh || exit 1;

RAW_ROOT=$1
RAW_SRC="https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/k9sxg2twv4-4.zip"

RAW_ZIP_FILE=${RAW_ROOT}/FOSD.zip
RAW_EXTRACT=${RAW_ROOT}/extracted
mkdir -p ${RAW_EXTRACT}

command -v curl >/dev/null 2>&1 ||\
    { echo "\"curl\" is needed but not found"'!'; exit 1; }

# curl -L ${RAW_SRC} --output ${RAW_ZIP_FILE}

# unzip ${RAW_ZIP_FILE} -d ${RAW_EXTRACT}

DATA_DST="data/all_vi"

mkdir -p ${DATA_DST}

echo ${RAW_EXTRACT}
echo ${DATA_DST}

local/move_raw_to_data_dst.py ${RAW_EXTRACT} ${DATA_DST}