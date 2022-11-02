GAZEBO_INCLUDE_DIR=$(pkg-config gazebo --cflags 2>/dev/null | cut -d' ' -f8 | cut -d'I' -f2)

rm -rf pygazebo/msg/*_pb2.py
cd pygazebo/msg

for DEFINITION in $(find ${GAZEBO_INCLUDE_DIR}/gazebo/msgs/proto -name '*.proto')
do 	
	echo "DEFINITION"
	echo $DEFINITION
	protoc -I ${GAZEBO_INCLUDE_DIR}/gazebo/msgs/proto --python_out=pygazebo/msg $DEFINITION
	for file in *
    do 
		PROTONAME=`echo ${file} | rev | cut -c4- | rev`
		echo $PROTONAME
		LC_ALL=C sed -i '' "s/import ${protoname}/from . import ${protoname}/g" *_pb2.py
	done
done
