import 'package:e_home/main.dart';
import 'package:e_home/screens/Screen_Roompage/components/devices_view.dart';
import 'package:e_home/screens/shared_components/text_with_pre_icon.dart';
import 'package:intl/intl.dart';
import 'package:e_home/screens/Screen_Statistics/statistics_scr.dart';
import 'package:flutter/material.dart';
import 'package:e_home/screens/shared_components/resident_avt.dart';
import 'package:flutter/widgets.dart';
import 'package:flutter/src/widgets/image.dart';
import 'background.dart';

// Import models
import 'package:e_home/models/Room.dart';

class Body extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // This size provides us total height and width of our screen
    Size size = MediaQuery.of(context).size;

    //Get today date in expected format
    var date = new DateFormat.yMMMMd('en_US').format(DateTime.now()).toString();
    String finalDate = date.toString();

    //Get data from Homepage
    int key = ModalRoute.of(context).settings.arguments as int;
    Room receivedRoom = RoomsModel.roomsData[key];

    return Background(
      child: Column(
        children: [
          SizedBox(
            height: size.height * 0.025,
          ),
          Padding(
            padding: const EdgeInsets.fromLTRB(10.0, 0.0, 10.0, 0.0),
            child: Row(
              children: [
                Text(
                  '${receivedRoom.name}',
                  style: Theme.of(context).textTheme.headline1.copyWith(
                        fontSize: size.height * 0.064,
                      ),
                ),
                Spacer(),
                ResidentAvt(
                  image: 'assets/images/Homepage/tham_avt.jpeg',
                  radius: size.height * 0.03,
                ),
              ],
            ),
          ),
          SizedBox(
            height: size.height * 0.01,
          ),
          Text(
            '${receivedRoom.tempSensors.value}°C',
            textAlign: TextAlign.center,
            style: Theme.of(context).textTheme.headline3,
          ),
          Text(
            "${finalDate}",
            style: TextStyle(fontSize: 20),
            textAlign: TextAlign.center,
          ),
          SizedBox(
            height: size.height * 0.03,
          ),
          Container(
            alignment: Alignment.center,
            height: size.height * 0.15,
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                TextWithPreIcon(
                  spaceSize: size.width * 0.015,
                  indentSize: size.width * 0.27,
                  icon: Icon(
                    Icons.volume_up_outlined,
                    size: size.height * 0.06,
                    color: Color.fromRGBO(45, 156, 219, 1.0),
                  ),
                  text: Text(
                    '${receivedRoom.soundSensors.value} dB',
                    style: Theme.of(context).textTheme.bodyText1.copyWith(
                          fontSize: size.height * 0.05,
                        ),
                  ),
                ),
                TextWithPreIcon(
                  spaceSize: size.width * 0.015,
                  indentSize: size.width * 0.22,
                  icon: Icon(
                    Icons.lightbulb_outlined,
                    size: size.height * 0.06,
                    color: Color.fromRGBO(255, 255, 51, 1.0),
                  ),
                  text: Text(
                    '${receivedRoom.lightSensors.value} Lux',
                    style: Theme.of(context).textTheme.bodyText1.copyWith(
                          fontSize: size.height * 0.05,
                        ),
                  ),
                ),
              ],
            ),
          ),
          SizedBox(
            height: size.height * 0.07,
          ),
          Container(
            alignment: Alignment.center,
            padding: const EdgeInsets.fromLTRB(30.0, 0.0, 10.0, 0.0),
            child: Text(
              'You should turn off the air conditioner and get rid of the loud noise',
              style: Theme.of(context)
                  .textTheme
                  .bodyText1
                  .copyWith(fontSize: size.height * 0.02),
            ),
          ),
          SizedBox(
            height: size.height * 0.03,
          ),
          DevicesView(receivedRoom),
          SizedBox(
            height: size.height * 0.025,
          ),
          Container(
            alignment: Alignment.bottomLeft,
            padding: const EdgeInsets.fromLTRB(20.0, 0.0, 0.0, 0.0),
            child: Ink(
              decoration: const ShapeDecoration(
                color: Colors.white,
                shape: CircleBorder(),
              ),
              child: IconButton(
                icon: const Icon(Icons.analytics_outlined),
                iconSize: 40,
                onPressed: () {
                  Navigator.pushNamed(context, '/statistics-screen',
                      arguments: key);
                },
              ),
            ),
          ),
        ],
      ),
    );
  }
}
