package com.example.kbr27.project;

import android.graphics.Color;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.ViewGroup;

import net.daum.mf.map.api.CameraUpdateFactory;
import net.daum.mf.map.api.MapPOIItem;
import net.daum.mf.map.api.MapPoint;
import net.daum.mf.map.api.MapPointBounds;
import net.daum.mf.map.api.MapPolyline;
import net.daum.mf.map.api.MapView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //지도 띄우기
        MapView mapView = new MapView(this);
        ViewGroup mapViewContainer = (ViewGroup) findViewById(R.id.map_view);
        mapViewContainer.addView(mapView);

        //중심점 변경
        mapView.setMapCenterPoint(MapPoint.mapPointWithGeoCoord(37.5136519, 126.9947909), true);

        //마커
        MapPOIItem marker = new MapPOIItem();
        marker.setItemName("반포대교");
        marker.setTag(0);
        marker.setMapPoint(MapPoint.mapPointWithGeoCoord(37.5136519, 126.9947909));
        marker.setMarkerType(MapPOIItem.MarkerType.RedPin); // 기본으로 제공하는 BluePin 마커 모양.
        marker.setSelectedMarkerType(MapPOIItem.MarkerType.BluePin); // 마커를 클릭했을때, 기본으로 제공하는 RedPin 마커 모양.
        mapView.addPOIItem(marker);

        //마커2
        MapPOIItem marker2 = new MapPOIItem();
        marker2.setItemName("경리단길");
        marker2.setTag(0);
        marker2.setMapPoint(MapPoint.mapPointWithGeoCoord(37.538432, 126.9853579));
        marker2.setMarkerType(MapPOIItem.MarkerType.BluePin); // 기본으로 제공하는 BluePin 마커 모양.
        marker2.setSelectedMarkerType(MapPOIItem.MarkerType.RedPin); // 마커를 클릭했을때, 기본으로 제공하는 RedPin 마커 모양.
        mapView.addPOIItem(marker2);

        //마커3
        MapPOIItem marker3 = new MapPOIItem();
        marker3.setItemName("국립중앙박물관");
        marker3.setTag(0);
        marker3.setMapPoint(MapPoint.mapPointWithGeoCoord(37.5239036, 126.9786427));
        marker3.setMarkerType(MapPOIItem.MarkerType.BluePin); // 기본으로 제공하는 BluePin 마커 모양.
        marker3.setSelectedMarkerType(MapPOIItem.MarkerType.RedPin); // 마커를 클릭했을때, 기본으로 제공하는 RedPin 마커 모양.
        mapView.addPOIItem(marker3);

        //마커4
        MapPOIItem marker4 = new MapPOIItem();
        marker4.setItemName("고속터미널역");
        marker4.setTag(0);
        marker4.setMapPoint(MapPoint.mapPointWithGeoCoord(37.5049142, 127.0027264));
        marker4.setMarkerType(MapPOIItem.MarkerType.BluePin); // 기본으로 제공하는 BluePin 마커 모양.
        marker4.setSelectedMarkerType(MapPOIItem.MarkerType.RedPin); // 마커를 클릭했을때, 기본으로 제공하는 RedPin 마커 모양.
        mapView.addPOIItem(marker4);

        //선 연결하기
        MapPolyline polyline = new MapPolyline();
        polyline.setTag(1000);
        polyline.setLineColor(Color.argb(128, 255, 51, 0)); // Polyline 컬러 지정.

        // Polyline 좌표 지정.
        polyline.addPoint(MapPoint.mapPointWithGeoCoord(37.538432, 126.9853579));
        polyline.addPoint(MapPoint.mapPointWithGeoCoord(37.5239036,126.9786427));
        polyline.addPoint(MapPoint.mapPointWithGeoCoord(37.5049142,127.0027264));

        // Polyline 지도에 올리기.
        mapView.addPolyline(polyline);

        // 지도뷰의 중심좌표와 줌레벨을 Polyline이 모두 나오도록 조정.
        MapPointBounds mapPointBounds = new MapPointBounds(polyline.getMapPoints());
        int padding = 100; // px
        mapView.moveCamera(CameraUpdateFactory.newMapPointBounds(mapPointBounds, padding));


    }
}

