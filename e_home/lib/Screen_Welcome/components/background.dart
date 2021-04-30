import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';

class Background extends StatelessWidget {
  final Widget child;

  const Background({
    Key key,
    @required this.child,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // This size provides us total height and width of our screen
    Size size = MediaQuery.of(context).size;

    return SafeArea(
      child: Padding(
        padding: const EdgeInsets.all(8.0),
        child: Container(
          height: size.height,
          width: double.infinity,
          child: SingleChildScrollView(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.center,
              children: <Widget>[
                SvgPicture.asset(
                  'assets/images/Welcome/Home_image.svg',
                  width: size.width,
                ),
                child,
              ],
            ),
          ),
        ),
      ),
    );
  }
}
